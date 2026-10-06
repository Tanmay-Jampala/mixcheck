# tests/task10.py
# Task: nth Fibonacci number (0th is 0, 1st is 1)
FUNCTION = "fibonacci"

CASES = [
    ([6], 8),                               # normal number (example from the task)
    ([0], 0),                               # the 0th number is 0
    ([1], 1),                               # the 1st number is 1
    ([2], 1),                               # first number made by adding the two before it
    ([10], 55),                             # bigger number
    ([20], 6765),                           # even bigger number
]
