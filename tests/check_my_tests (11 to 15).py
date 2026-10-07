# Scratch checker: runs every test file against a known-correct solution.
# Run from the project root (the folder that contains tests/):  python check_my_tests.py
# Every line must say OK.  Do NOT commit this file.
import importlib


# ---- correct solutions (one per task) ----
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def capitalize_words(sentence):
    return " ".join(w.capitalize() for w in sentence.split(" "))


def word_count(sentence):
    counts = {}
    for w in sentence.split():
        counts[w] = counts.get(w, 0) + 1
    return counts


def are_anagrams(a, b):
    return sorted(a) == sorted(b)


def missing_number(nums):
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)


SOLUTIONS = {
    "task11": celsius_to_fahrenheit,
    "task12": capitalize_words,
    "task13": word_count,
    "task14": are_anagrams,
    "task15": missing_number,
}

all_ok = True
for task, solution in SOLUTIONS.items():
    mod = importlib.import_module(f"tests.{task}")
    FUNCTION, CASES = mod.FUNCTION, mod.CASES
    if solution.__name__ != FUNCTION:
        print(f"{task}: FUNCTION is '{FUNCTION}' but solution is '{solution.__name__}'  <-- check the name")
        all_ok = False
        continue
    print(f"--- {task} ({FUNCTION}) ---")
    for inputs, expected in CASES:
        try:
            got = solution(*inputs)
        except Exception as e:
            got = f"ERROR: {e}"
        ok = got == expected
        all_ok = all_ok and ok
        print(f"{'OK  ' if ok else 'FAIL'} {inputs!r} -> expected {expected!r}, got {got!r}")

print("\nALL OK" if all_ok else "\nSOME FAILED - fix before committing")
