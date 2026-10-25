# tests/task17.py
# Task: Indian mobile number: optional +91 or 0, then 10 digits starting 6-9
FUNCTION = "valid_mobile"

CASES = [
    (["9876543210"], True),  # plain 10 digits
    (["+91 98765 43210"], True),  # the example: +91 and spaces
    (["09876543210"], True),  # leading 0
    (["+919876543210"], True),  # +91 with no spaces
    (["5876543210"], False),  # starts with 5
    (["98765 4321"], False),  # only 9 digits
    (["+91987654321a"], False),  # contains a letter
    (["919876543210"], False),  # 91 without the + is not a prefix
    ([""], False),  # empty string
]
