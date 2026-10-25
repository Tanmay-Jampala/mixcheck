# tests/task25.py
# Task: balance after each transaction, skip withdrawals that go below zero
FUNCTION = "running_balance"

CASES = [
    ([["+500", "-200", "-500"], 100], [600, 400, 400]),  # the example: the last withdrawal would go below zero
    ([[], 50], []),  # no transactions
    ([["-10"], 5], [5]),  # a withdrawal that would go below zero is skipped
    ([["+0", "-0"], 0], [0, 0]),  # zero amounts
    ([["+100", "-100", "-1"], 0], [100, 0, 0]),  # exactly zero is allowed, below zero is not
    ([["+500", "-200", "-400"], 100], [600, 400, 0]),  # withdrawing down to exactly zero is allowed
]
