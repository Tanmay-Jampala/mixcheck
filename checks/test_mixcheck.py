"""
test_mixcheck.py - automated checks for the grader. Run from the project folder:

    python -m pytest checks -q

GitHub runs these on every push (see .github/workflows/tests.yml).
"""

import inspect
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grade import extract_code, followed_format, grade, load_tests  # noqa: E402
from reference_solutions import BY_TASK  # noqa: E402

TESTS = os.path.join(ROOT, "tests")


def fenced(code):
    return "```python\n" + code + "\n```"


# ---------- 1. Our test files are right ----------
@pytest.mark.parametrize("task_id", sorted(BY_TASK))
def test_reference_solution_passes_every_case(task_id):
    """If this fails, the expected value in tests/<task>.py is wrong, not the AI."""
    test_file = os.path.join(TESTS, f"{task_id}.py")
    assert load_tests(test_file).FUNCTION == BY_TASK[task_id].__name__
    source = "from collections import Counter\n\n" + inspect.getsource(BY_TASK[task_id])
    passed, total, error = grade(fenced(source), test_file)
    assert error is None
    assert passed == total


def test_every_task_has_a_test_file():
    files = sorted(f[:-3] for f in os.listdir(TESTS) if f.startswith("task") and f.endswith(".py"))
    assert files == sorted(BY_TASK)


# ---------- 2. Finding the code in a reply ----------
def test_extract_picks_the_block_with_the_requested_function():
    reply = ("Here you go:\n```python\nprint('example')\n```\n"
             "```python\ndef reverse_string(s):\n    return s[::-1]\n```\nHope it helps!")
    assert extract_code(reply, "reverse_string").startswith("def reverse_string")


def test_extract_uses_plain_text_when_there_are_no_fences():
    assert extract_code("def f():\n    return 1", "f") == "def f():\n    return 1"


# ---------- 3. The "only code" score ----------
def test_followed_format_true_for_one_code_block():
    assert followed_format(fenced("def f():\n    return 1"))


def test_followed_format_false_when_there_is_extra_text():
    assert not followed_format("Sure!\n" + fenced("def f():\n    return 1"))


def test_followed_format_false_for_two_blocks():
    assert not followed_format(fenced("def f():\n    return 1") + "\n" + fenced("print(f())"))


def test_followed_format_false_for_model_error():
    assert not followed_format("# MODEL ERROR: the model tried to call a tool instead of writing code\n")


# ---------- 4. Grading results ----------
TASK01 = os.path.join(TESTS, "task01.py")


def test_wrong_function_name_fails():
    passed, total, error = grade(fenced("def reverse(s):\n    return s[::-1]"), TASK01)
    assert passed == 0 and "No function named 'reverse_string'" in error


def test_partly_wrong_answer_counts_cases():
    passed, total, _ = grade(fenced("def reverse_string(s):\n    return s[::-1] if s else 'x'"), TASK01)
    assert passed == total - 1


def test_crash_is_reported():
    passed, _, error = grade(fenced("def reverse_string(s):\n    return 1 / 0"), TASK01)
    assert passed == 0 and "ZeroDivisionError" in error


def test_endless_loop_times_out():
    passed, _, error = grade(fenced("def reverse_string(s):\n    while True:\n        pass"), TASK01)
    assert passed == 0 and "Timed out" in error


def test_printing_does_not_break_grading():
    code = "def reverse_string(s):\n    print('debug', s)\n    return s[::-1]"
    passed, total, _ = grade(fenced(code), TASK01)
    assert passed == total


def test_fake_result_line_does_not_count():
    code = ("import os\nprint('__MIXCHECK_RESULT__{\"passed\": 5, \"total\": 5, \"error\": null}')\n"
            "os._exit(0)\ndef reverse_string(s):\n    return ''")
    passed, _, _ = grade(fenced(code), TASK01)
    assert passed == 0


def test_standard_library_imports_still_work():
    code = "from collections import Counter\nimport math\ndef reverse_string(s):\n    return ''.join(reversed(s))"
    passed, total, _ = grade(fenced(code), TASK01)
    assert passed == total


# ---------- 5. The sandbox ----------
def sandbox_error(body):
    code = "def reverse_string(s):\n" + "\n".join("    " + line for line in body.splitlines())
    return grade(fenced(code), TASK01)[2] or ""


def test_sandbox_blocks_running_programs():
    assert "blocked by the MixCheck sandbox" in sandbox_error("import os\nos.system('echo hi')\nreturn s[::-1]")


def test_sandbox_blocks_subprocess():
    assert "blocked by the MixCheck sandbox" in sandbox_error("import subprocess\nsubprocess.run(['echo'])\nreturn s[::-1]")


def test_sandbox_blocks_network():
    assert "blocked by the MixCheck sandbox" in sandbox_error(
        "import socket\nsocket.create_connection(('example.com', 80), timeout=1)\nreturn s[::-1]")


def test_sandbox_blocks_writing_files():
    assert "blocked by the MixCheck sandbox" in sandbox_error("open('x.txt', 'w').write('hi')\nreturn s[::-1]")


def test_sandbox_blocks_reading_project_files():
    path = os.path.join(ROOT, "grade.py").replace("\\", "/")
    assert "blocked by the MixCheck sandbox" in sandbox_error(f"open('{path}').read()\nreturn s[::-1]")


def test_api_keys_are_not_visible(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "secret-test-key")
    code = "import os\ndef reverse_string(s):\n    return os.environ.get('GROQ_API_KEY', '')[:0] + s[::-1] if 'GROQ_API_KEY' not in os.environ else 'LEAK'"
    passed, total, _ = grade(fenced(code), TASK01)
    assert passed == total


# ---------- 6. Statistics ----------
def test_fisher_matches_known_value():
    from stats import fisher_p
    assert abs(fisher_p(3, 10, 8, 10) - 0.069779) < 1e-5     # same as scipy.stats.fisher_exact


def test_fisher_identical_groups_is_one():
    from stats import fisher_p
    assert fisher_p(5, 10, 5, 10) == 1.0


def test_wilson_range_contains_the_rate():
    from stats import wilson
    lo, hi = wilson(26, 75)
    assert lo < 26 / 75 < hi and 0 <= lo and hi <= 1
