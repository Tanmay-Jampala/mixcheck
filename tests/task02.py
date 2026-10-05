# tests/task02.py
# Task: count vowels (a, e, i, o, u, uppercase or lowercase)
FUNCTION = "count_vowels"

CASES = [
    (["Apple"], 2),                         # normal word (example from the task)
    ([""], 0),                              # empty string
    (["a"], 1),                             # one character
    (["AEIOU"], 5),                         # all uppercase vowels
    (["rhythm"], 0),                        # no vowels
    (["sky"], 0),                           # "y" is NOT a vowel in this task
    (["Hello World"], 3),                   # spaces, mixed case
]
