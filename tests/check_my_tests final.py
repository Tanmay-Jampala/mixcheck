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

def sum_even_numbers(numbers):
    return sum(n for n in numbers if n % 2 == 0)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def second_largest(numbers):
    if len(numbers) < 2:
        return None
    return sorted(numbers)[-2]

def count_words(s):
    return len(s.split())

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for n in range(1, 11):
    module = importlib.import_module(f"tests.task{n:02d}")
    func = globals()[module.FUNCTION]
    print(f"--- task{n:02d}: {module.FUNCTION}")
    for args, expected in module.CASES:
        result = func(*args)
        print(args, "->", result, "OK" if result == expected else f"WRONG, expected {expected}")
