# tests/task08.py
# Task: second-largest number in a list of distinct numbers (None if fewer than two numbers)
FUNCTION = "second_largest"

# Note the double brackets: the function takes ONE input, and that input is a list.
CASES = [
    ([[10, 4, 7, 2]], 7),                   # normal list (example from the task)
    ([[]], None),                           # empty list: fewer than two numbers
    ([[5]], None),                          # one item: fewer than two numbers
    ([[1, 2]], 1),                          # exactly two numbers
    ([[9, 8, 7]], 8),                       # already sorted, biggest first
    ([[-5, -1, -3]], -3),                   # all negative numbers
]
