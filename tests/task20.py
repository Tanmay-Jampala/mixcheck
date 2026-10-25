# tests/task20.py
# Task: run-length: char + count, no number for single chars
FUNCTION = "compress"

CASES = [
    (["aaabccdddd"], "a3bc2d4"),  # the example from the task
    ([""], ""),  # empty string
    (["abc"], "abc"),  # no repeats: no numbers
    (["aabbaa"], "a2b2a2"),  # the same letter in two separate runs
    (["zzzzzzzzzzzz"], "z12"),  # a two-digit count
]
