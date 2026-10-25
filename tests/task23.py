# tests/task23.py
# Task: A/B/C/D/F bands, Invalid outside 0-100
FUNCTION = "grade_from_marks"

CASES = [
    ([100], "A"),  # top
    ([90], "A"),  # lowest A
    ([89], "B"),  # highest B
    ([75], "B"),  # the example
    ([74], "C"),  # highest C
    ([60], "C"),  # lowest C
    ([59], "D"),  # highest D
    ([40], "D"),  # lowest D
    ([39], "F"),  # highest F
    ([0], "F"),  # zero
    ([-1], "Invalid"),  # below 0
    ([101], "Invalid"),  # above 100
]
