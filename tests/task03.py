# tests/task03.py
# Task: find the largest number in a list (None if the list is empty)
FUNCTION = "find_largest"

# Note the double brackets: the function takes ONE input, and that input is a list.
CASES = [
    ([[3, 9, 2]], 9),                       # normal list (example from the task)
    ([[]], None),                           # empty list: the tricky case
    ([[5]], 5),                             # one item
    ([[-3, -1, -7]], -1),                   # all negative numbers
    ([[2, 7, 7, 1]], 7),                    # duplicate largest value
]
