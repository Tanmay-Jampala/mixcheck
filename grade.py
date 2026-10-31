"""
grade.py - checks whether AI-written code actually works.

Use it like this:
    passed, total, error = grade(ai_reply_text, "tests/task01.py")
"""

import importlib.util
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile

TIMEOUT_SECONDS = 10

# A special label the helper script puts in front of its result,
# so we can find the result even if the AI's code prints other things.
RESULT_MARKER = "__MIXCHECK_RESULT__"


# ---------------------------------------------------------------
# Part 1: find the code in the AI's reply
# ---------------------------------------------------------------
FENCE = r"```[a-zA-Z0-9]*[ \t]*\n(.*?)```"


def code_blocks(reply_text):
    return re.findall(FENCE, reply_text, flags=re.DOTALL)


def extract_code(reply_text, function_name=None):
    """Return the code we should test.

    Replies often contain several code blocks (the function, then usage examples,
    then sample output). Like standard benchmarks, we test the block that defines
    the function we asked for. If there are no ``` fences, the reply is the code."""
    blocks = code_blocks(reply_text)
    if not blocks:
        return reply_text.strip()
    if function_name:
        for block in blocks:
            if re.search(rf"\bdef\s+{re.escape(function_name)}\s*\(", block):
                return block.strip()
    for block in blocks:
        if re.search(r"\bdef\s+\w+\s*\(", block):
            return block.strip()
    return blocks[0].strip()


def strip_fences(reply_text):
    """Kept for older code: the first block that defines a function."""
    return extract_code(reply_text)


def followed_format(reply_text):
    """Did the AI do what we asked, "reply with only the code"?
    True if the reply is exactly one code block with nothing around it,
    or plain code with no fences at all."""
    text = reply_text.strip()
    if text.startswith("# MODEL ERROR"):
        return False
    blocks = code_blocks(text)
    if blocks:
        outside = re.sub(r"```[a-zA-Z0-9]*[ \t]*\n.*?```", "", text, flags=re.DOTALL).strip()
        return len(blocks) == 1 and outside == ""
    try:
        compile(text, "reply", "exec")
        return True
    except (SyntaxError, ValueError):
        return False


# ---------------------------------------------------------------
# Part 2: read FUNCTION and CASES from a test file like tests/task01.py
# ---------------------------------------------------------------
def load_tests(test_file):
    spec = importlib.util.spec_from_file_location("test_module", test_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------
# Part 3: the helper script that runs in a SEPARATE process.
# It loads the AI's code, calls the function on every case,
# and prints the score with RESULT_MARKER + a secret code in front.
#
# Safety layers (the AI's code is untrusted):
#   1. separate process with a time limit       -> a crash or endless loop can't hurt the app
#   2. clean environment (-I, no API keys)       -> the code can't read our secrets
#   3. Python audit hook                         -> blocks network, running programs,
#                                                   deleting/writing files, ctypes
#   4. memory limit (Linux, e.g. Streamlit Cloud) -> can't eat all the RAM
#   5. secret per-run code on the result line    -> printing a fake "passed" line doesn't work
# ---------------------------------------------------------------
RUNNER_CODE = r"""
import copy, importlib.util, json, os, sys

def main():
    secret = sys.stdin.readline().strip()        # only the grader knows this
    write = sys.__stdout__.write                 # keep our own handle on stdout
    flush = sys.__stdout__.flush
    test_path, solution_path = sys.argv[1], sys.argv[2]

    spec = importlib.util.spec_from_file_location("test_module", test_path)
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    function_name, cases = tests.FUNCTION, copy.deepcopy(tests.CASES)
    result = {"passed": 0, "total": len(cases), "error": None}

    def finish():
        write("__MIXCHECK_RESULT__" + secret + json.dumps(result) + "\n")
        flush()
        os._exit(0)

    with open(solution_path, encoding="utf-8") as f:
        source = f.read()

    # Layer 4: memory limit (works on Linux; skipped on Windows)
    try:
        import resource
        limit = 1024 * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    except Exception:
        pass

    # Layer 3: block dangerous actions from here on
    blocked = ("subprocess.", "os.system", "os.exec", "os.spawn", "os.posix_spawn", "os.fork",
               "os.kill", "os.remove", "os.unlink", "os.rmdir", "os.rename", "os.chmod",
               "os.putenv", "os.unsetenv", "shutil.", "socket.", "urllib.", "http.", "ftplib.",
               "smtplib.", "ctypes.", "winreg.", "webbrowser.")
    write_flags = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | getattr(os, "O_TRUNC", 0)

    # Reading is allowed only inside Python itself and this run's temporary folder,
    # so the code can import the standard library but can't read our project or .env file
    readable = tuple(os.path.normcase(os.path.abspath(p)) for p in
                     {sys.prefix, sys.base_prefix, sys.exec_prefix, os.path.dirname(solution_path)})

    def guard(event, args):
        if event.startswith(blocked):
            raise PermissionError("blocked by the MixCheck sandbox: " + event)
        if event == "open":
            path = args[0] if args else None
            mode = args[1] if len(args) > 1 else None
            flags = args[2] if len(args) > 2 else None
            writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or \
                      (isinstance(flags, int) and flags & write_flags)
            if writing:
                raise PermissionError("blocked by the MixCheck sandbox: writing files")
            if isinstance(path, (str, bytes)):
                full = os.path.normcase(os.path.abspath(os.fsdecode(path)))
                if not full.startswith(readable):
                    raise PermissionError("blocked by the MixCheck sandbox: reading files outside Python")

    sys.dont_write_bytecode = True
    sys.addaudithook(guard)

    namespace = {"__name__": "ai_solution"}
    try:
        exec(compile(source, "ai_code.py", "exec"), namespace)
    except BaseException as e:
        result["error"] = "The code crashed while loading: " + type(e).__name__ + ": " + str(e)
        finish()

    func = namespace.get(function_name)
    if not callable(func):
        result["error"] = "No function named '" + function_name + "' in the AI's code"
        finish()

    for args, expected in cases:
        try:
            actual = func(*copy.deepcopy(args))
            if actual == expected:
                result["passed"] += 1
        except BaseException as e:
            if result["error"] is None:
                result["error"] = ("Crashed on input " + repr(args) + ": "
                                   + type(e).__name__ + ": " + str(e))
    finish()

main()
"""

# Only these environment variables reach the AI's code (no API keys)
SAFE_ENV_VARS = ("PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "TMPDIR", "HOME", "USERPROFILE", "LANG")


# ---------------------------------------------------------------
# Part 4: the main function - grade(code_text, test_file)
# ---------------------------------------------------------------
def grade(code_text, test_file):
    """Returns (passed, total, error). error is None if nothing crashed."""
    tests = load_tests(test_file)
    total = len(tests.CASES)
    code = extract_code(code_text, tests.FUNCTION)

    with tempfile.TemporaryDirectory() as temp_folder:
        solution_path = os.path.join(temp_folder, "ai_solution.py")
        runner_path = os.path.join(temp_folder, "runner.py")
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(code)
        with open(runner_path, "w", encoding="utf-8") as f:
            f.write(RUNNER_CODE)

        env = {name: os.environ[name] for name in SAFE_ENV_VARS if name in os.environ}
        secret = secrets.token_hex(16)
        try:
            finished = subprocess.run(
                # -I: isolated mode (ignores PYTHON* settings and user packages), -X utf8: UTF-8 output
                [sys.executable, "-I", "-X", "utf8", runner_path, os.path.abspath(test_file), solution_path],
                input=secret + "\n",
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=TIMEOUT_SECONDS,
                cwd=temp_folder,
                env=env,
            )
        except subprocess.TimeoutExpired:
            return 0, total, f"Timed out after {TIMEOUT_SECONDS} seconds (maybe an infinite loop)"

    # Look for the result line the helper script printed
    tag = RESULT_MARKER + secret
    for line in reversed(finished.stdout.splitlines()):
        if line.startswith(tag):
            data = json.loads(line[len(tag):])
            return data["passed"], data["total"], data["error"]

    # No result line: the process died in some unexpected way
    last_lines = finished.stderr.strip().splitlines()[-3:]
    return 0, total, "Grader got no result. " + " ".join(last_lines)