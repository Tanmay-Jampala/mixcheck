"""
reference_solutions.py - our own correct answer for every task.

checks/test_mixcheck.py runs each of these through the real grader. If a reference ever
fails, the mistake is in our test file, not in the AI. (This is how we caught 2 wrong
expected values in our own tests.)
"""

from collections import Counter


def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


def find_largest(numbers):
    return max(numbers) if numbers else None


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def remove_duplicates(items):
    seen, out = set(), []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


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


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def capitalize_words(sentence):
    return " ".join(w[:1].upper() + w[1:] for w in sentence.split(" ")) if sentence else ""


def word_count(sentence):
    return dict(Counter(sentence.split()))


def are_anagrams(a, b):
    return sorted(a) == sorted(b)


def missing_number(numbers):
    n = len(numbers) + 1
    return n * (n + 1) // 2 - sum(numbers)


def indian_format(n):
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:])
        head = head[:-2]
    if head:
        groups.insert(0, head)
    return ",".join(groups + [tail])


def valid_mobile(s):
    s = s.replace(" ", "")
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]
    return len(s) == 10 and s.isdigit() and s[0] in "6789"


def sort_words(sentence):
    words = {w.lower() for w in sentence.split()}
    return sorted(words, key=lambda w: (len(w), w))


def minutes_between(start, end):
    def to_minutes(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)
    diff = to_minutes(end) - to_minutes(start)
    return diff if diff >= 0 else diff + 24 * 60


def compress(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(s[i] + (str(j - i) if j - i > 1 else ""))
        i = j
    return "".join(out)


def caesar_shift(s, k):
    out = []
    for c in s:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - 97 + k) % 26 + 97))
        elif "A" <= c <= "Z":
            out.append(chr((ord(c) - 65 + k) % 26 + 65))
        else:
            out.append(c)
    return "".join(out)


def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals, key=lambda iv: iv[0]):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def grade_from_marks(marks):
    if marks < 0 or marks > 100:
        return "Invalid"
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


def second_most_common(s):
    chars = [c for c in s if c != " "]
    counts = Counter(chars)
    if len(counts) < 2:
        return None
    first_seen = {}
    for i, c in enumerate(chars):
        first_seen.setdefault(c, i)
    ranked = sorted(counts, key=lambda c: (-counts[c], first_seen[c]))
    return ranked[1]


def running_balance(transactions, balance):
    out = []
    for t in transactions:
        amount = int(t)
        if balance + amount >= 0:
            balance += amount
        out.append(balance)
    return out


# task number -> function, in the same order as tests/task01.py ... task25.py
BY_TASK = {f"task{i:02d}": fn for i, fn in enumerate([
    reverse_string, count_vowels, find_largest, is_palindrome, remove_duplicates,
    sum_even_numbers, factorial, second_largest, count_words, fibonacci,
    celsius_to_fahrenheit, capitalize_words, word_count, are_anagrams, missing_number,
    indian_format, valid_mobile, sort_words, minutes_between, compress,
    caesar_shift, merge_intervals, grade_from_marks, second_most_common, running_balance,
], start=1)}
