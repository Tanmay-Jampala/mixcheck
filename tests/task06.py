# tests/task06.py
# Task: sum of all even numbers in a list (0 if there are none)
FUNCTION = "sum_even_numbers"

# Note the double brackets: the function takes ONE input, and that input is a list.
CASES = [
    ([[1, 2, 3, 4, 5]], 6),                 # normal list (example from the task)
    ([[]], 0),                              # empty list
    ([[1, 3, 5]], 0),                       # no even numbers: must return 0
    ([[2, 4, 6]], 12),                      # all even numbers
    ([[0]], 0),                             # zero is even, adds nothing
    ([[-2, -3, 4]], 2),                     # negative even number counts too
    ([[7]], 0),                             # one odd item
]
