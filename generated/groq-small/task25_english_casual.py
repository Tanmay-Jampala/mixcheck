```python
def running_balance(transactions, start):
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        List of transaction strings, e.g. "+500" or "-200".
    start : int
        Opening balance.

    Returns
    -------
    list[int]
        Balance after each transaction.  If a withdrawal would
        bring the balance below zero, the transaction is skipped
        (balance stays the same) but the unchanged balance is still
        appended to the result list.
    """
    balance = start
    result = []

    for t in transactions:
        # Determine sign and amount
        sign = t[0]
        try:
            amount = int(t[1:])
        except ValueError:
            raise ValueError(f"Invalid transaction format: {t}")

        if sign == '+':
            balance += amount
        elif sign == '-':
            # Only apply if it doesn't go negative
            if balance - amount >= 0:
                balance -= amount
        else:
            raise ValueError(f"Transaction must start with '+' or '-': {t}")

        result.append(balance)

    return result
```