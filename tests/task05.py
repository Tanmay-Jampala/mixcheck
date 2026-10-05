# tests/task05.py
# Task: remove duplicates, keep first appearance, keep original order
FUNCTION = "remove_duplicates"

CASES = [
    ([[1, 2, 1, 3, 2]], [1, 2, 3]),        # normal list (example from the task)
    ([[]], []),                             # empty list
    ([[7]], [7]),                           # one item
    ([[1, 1, 1, 1]], [1]),                  # everything is a duplicate
    ([[3, 1, 3, 2, 1]], [3, 1, 2]),         # order must stay as first seen (not sorted)
    ([["a", "b", "a"]], ["a", "b"]),        # works with strings too
]
