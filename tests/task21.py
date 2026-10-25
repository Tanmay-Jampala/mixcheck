# tests/task21.py
# Task: shift letters k places, wrap z->a, keep case, leave other characters
FUNCTION = "caesar_shift"

CASES = [
    (["Hello, World!", 3], "Khoor, Zruog!"),  # the example from the task
    (["xyz", 3], "abc"),  # wrapping around
    (["ABC", 26], "ABC"),  # a full circle
    (["a1 b2", 1], "b1 c2"),  # digits and spaces stay
    (["", 5], ""),  # empty string
    (["Zz", 1], "Aa"),  # wrap keeps the case
]
