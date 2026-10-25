```python
def running_balance(transactions, start_balance):
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : list of str
        Each transaction is a string like "+500" or "-200".
    start_balance : int
        The initial balance.

    Returns
    -------
    list of int
        Balance after each transaction, with withdrawals that would
        cause a negative balance ignored (balance unchanged but still recorded).
    """
    balance = start_balance
    result = []

    for txn in transactions:
        # Parse the sign and amount
        sign = txn[0]
        amount = int(txn[1:])

        if sign == '+':
            balance += amount
        elif sign == '-':
            # Only apply withdrawal if it doesn't make the balance negative
            if balance - amount >= 0:
                balance -= amount
            # else: balance stays the same
        else:
            raise ValueError(f"Invalid transaction format: {txn}")

        result.append(balance)

    return result
```