# tests/task04.py
# Task: is_palindrome (no spaces, uppercase/lowercase treated the same)
FUNCTION = "is_palindrome"

CASES = [
    (["Racecar"], True),                    # normal palindrome (example from the task)
    (["hello"], False),                     # normal non-palindrome
    (["a"], True),                          # one character
    (["Aa"], True),                         # capitals: A and a count as the same
    (["ab"], False),                        # two different characters
    # ([""], True),                         # empty string: unclear in the task, enable ONLY after Aaditya confirms
]
