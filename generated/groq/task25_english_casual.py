```python
def running_balance(transactions, start):
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        List of transaction strings, e.g. "+500" or "-200".
    start : int or float
        Opening balance.

    Returns
    -------
    list[int|float]
        Balance after each transaction. If a withdrawal would cause the
        balance to drop below zero, the transaction is ignored (balance
        stays the same) but the unchanged balance is still recorded.
    """
    balance = start
    balances = []

    for txn in transactions:
        # Parse the sign and amount
        sign = txn[0]
        amount = float(txn[1:]) if '.' in txn else int(txn[1:])

        if sign == '+':
            balance += amount
        elif sign == '-':
            # Skip withdrawal that would make balance negative
            if balance - amount >= 0:
                balance -= amount
        else:
            raise ValueError(f"Invalid transaction format: {txn}")

        balances.append(balance)

    return balances
```