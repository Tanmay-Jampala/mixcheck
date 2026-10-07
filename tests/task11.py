FUNCTION = "celsius_to_fahrenheit"

# Only inputs that give exact answers (no 37 -> 98.60000000000001 problem)
CASES = [
    ([0], 32.0),        # freezing point
    ([100], 212.0),     # boiling point (the example from the task)
    ([-40], -40.0),     # the point where C and F are equal: the tricky case
    ([10], 50.0),       # normal positive value
    ([-10], 14.0),      # negative value, not -40
]
