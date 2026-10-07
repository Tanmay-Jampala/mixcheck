FUNCTION = "missing_number"

# The input is ONE list, so it sits inside the inputs list: [[3, 1, 4]]
CASES = [
    ([[3, 1, 4]], 2),         # the example from the task (n = 4, middle number missing)
    ([[1, 2, 3]], 4),         # last number missing: the tricky case (max(list) would give the wrong n)
    ([[2, 3, 4]], 1),         # first number missing
    ([[5, 3, 1, 2]], 4),      # any order, bigger list
    ([[2]], 1),               # smallest list (n = 2)
]
