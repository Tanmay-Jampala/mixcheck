# tests/task07.py
# Task: factorial of a non-negative integer (factorial of 0 is 1)
FUNCTION = "factorial"

CASES = [
    ([5], 120),                             # normal number (example from the task)
    ([0], 1),                               # zero: the tricky case, 0! is 1
    ([1], 1),                               # one
    ([3], 6),                               # small number
    ([10], 3628800),                        # bigger number
]
