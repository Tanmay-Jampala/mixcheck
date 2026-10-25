# tests/task16.py
# Task: Indian-style commas: last 3 digits, then groups of 2
FUNCTION = "indian_format"

CASES = [
    ([0], "0"),  # zero
    ([999], "999"),  # below 1000: no commas
    ([1000], "1,000"),  # first comma
    ([1234567], "12,34,567"),  # the example from the task
    ([100000], "1,00,000"),  # one lakh
    ([12345678901], "12,34,56,78,901"),  # a long number
]
