# tests/task22.py
# Task: merge overlapping or touching intervals, sorted by start
FUNCTION = "merge_intervals"

CASES = [
    ([[[1, 3], [2, 6], [8, 10]]], [[1, 6], [8, 10]]),  # the example from the task
    ([[]], []),  # no intervals
    ([[[1, 4], [4, 5]]], [[1, 5]]),  # touching intervals merge
    ([[[5, 6], [1, 2]]], [[1, 2], [5, 6]]),  # unsorted input
    ([[[1, 10], [2, 3], [4, 5]]], [[1, 10]]),  # one interval swallows the others
]
