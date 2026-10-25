```python
def running_balance(start_balance: int, transactions: list[str]) -> list[int]:
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    start_balance : int
        The initial amount of money.
    transactions : list[str]
        A list of transaction strings, e.g. ["+500", "-200", "-800"].
        A leading '+' means a deposit, '-' means a withdrawal.

    Returns
    -------
    list[int]
        Balance after each transaction. If a withdrawal would make the
        balance drop below zero, the transaction is ignored but the
        current balance is still recorded in the output list.
    """
    balance = start_balance
    balances = []

    for tx in transactions:
        # Strip whitespace and ensure the sign is present
        tx = tx.strip()
        if not tx:
            continue

        sign = tx[0]
        amount = int(tx[1:])  # assumes well‑formed input like "+500" or "-200"

        if sign == '+':
            balance += amount
        elif sign == '-':
            # Apply only if it doesn't make the balance negative
            if balance - amount >= 0:
                balance -= amount
            # else: skip the withdrawal (balance stays the same)
        else:
            raise ValueError(f"Invalid transaction format: {tx}")

        balances.append(balance)

    return balances
```