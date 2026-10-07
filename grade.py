"""
grade.py - checks whether AI-written code actually works.

Use it like this:
    passed, total, error = grade(ai_reply_text, "tests/task01.py")
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

TIMEOUT_SECONDS = 10

# A special label the helper script puts in front of its result,
# so we can find the result even if the AI's code prints other things.
RESULT_MARKER = "__MIXCHECK_RESULT__"


# ---------------------------------------------------------------
# Part 1: remove the ```python ... ``` fences from the AI's reply
# ---------------------------------------------------------------
def strip_fences(reply_text):
    """Return only the code inside ``` fences. If there are no fences,
    return the reply as it is."""
    pattern = r"```[a-zA-Z0-9]*[ \t]*\n(.*?)```"
    blocks = re.findall(pattern, reply_text, flags=re.DOTALL)
    if blocks:
        return "\n\n".join(blocks).strip()
    return reply_text.strip()


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
# and prints the score with RESULT_MARKER in front.
# ---------------------------------------------------------------
RUNNER_CODE = '''
import copy, importlib.util, json, sys

MARKER = "__MIXCHECK_RESULT__"
test_path, solution_path = sys.argv[1], sys.argv[2]

spec = importlib.util.spec_from_file_location("test_module", test_path)
tests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tests)

result = {"passed": 0, "total": len(tests.CASES), "error": None}

def finish():
    print(MARKER + json.dumps(result))
    sys.exit(0)

# Load the AI's code
with open(solution_path, encoding="utf-8") as f:
    source = f.read()
namespace = {"__name__": "ai_solution"}
try:
    exec(compile(source, "ai_code.py", "exec"), namespace)
except Exception as e:
    result["error"] = "The code crashed while loading: " + type(e).__name__ + ": " + str(e)
    finish()

# Find the function we are testing
func = namespace.get(tests.FUNCTION)
if not callable(func):
    result["error"] = "No function named '" + tests.FUNCTION + "' in the AI's code"
    finish()

# Try every case
for args, expected in tests.CASES:
    try:
        actual = func(*copy.deepcopy(args))
        if actual == expected:
            result["passed"] += 1
    except Exception as e:
        if result["error"] is None:
            result["error"] = ("Crashed on input " + repr(args) + ": "
                               + type(e).__name__ + ": " + str(e))

finish()
'''


# ---------------------------------------------------------------
# Part 4: the main function - grade(code_text, test_file)
# ---------------------------------------------------------------
def grade(code_text, test_file):
    """Returns (passed, total, error). error is None if nothing crashed."""
    total = len(load_tests(test_file).CASES)
    code = strip_fences(code_text)

    with tempfile.TemporaryDirectory() as temp_folder:
        solution_path = os.path.join(temp_folder, "ai_solution.py")
        runner_path = os.path.join(temp_folder, "runner.py")
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(code)
        with open(runner_path, "w", encoding="utf-8") as f:
            f.write(RUNNER_CODE)

        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        try:
            finished = subprocess.run(
                [sys.executable, runner_path, os.path.abspath(test_file), solution_path],
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
    for line in reversed(finished.stdout.splitlines()):
        if line.startswith(RESULT_MARKER):
            data = json.loads(line[len(RESULT_MARKER):])
            return data["passed"], data["total"], data["error"]

    # No result line: the process died in some unexpected way
    last_lines = finished.stderr.strip().splitlines()[-3:]
    return 0, total, "Grader got no result. " + " ".join(last_lines)