# check_my_tests.py: scratch file, don't commit
# Run from the main project folder:  python check_my_tests.py
import importlib

# Known-correct solutions. If one of these fails a test, the TEST is wrong.
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

for n in range(1, 6):
    module = importlib.import_module(f"tests.task{n:02d}")
    func = globals()[module.FUNCTION]
    print(f"--- task{n:02d}: {module.FUNCTION}")
    for args, expected in module.CASES:
        result = func(*args)
        print(args, "->", result, "OK" if result == expected else f"WRONG, expected {expected}")
