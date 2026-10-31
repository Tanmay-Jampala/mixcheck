```python
def running_balance(transactions, start_balance):
    """
    Calculate the running balance after each transaction.

    Parameters
    ----------
    transactions : list of str
        Each transaction is a string like "+500" or "-200".
    start_balance : int
        The initial balance before any transactions.

    Returns
    -------
    list of int
        The balance after each transaction. If a withdrawal would
        bring the balance below zero, that transaction is skipped
        (balance remains unchanged) but the unchanged balance is
        still appended to the result list.
    """
    balance = start_balance
    result = []

    for t in transactions:
        t = t.strip()
        if not t:
            continue  # skip empty strings

        sign = t[0]
        try:
            amount = int(t[1:])
        except ValueError:
            raise ValueError(f"Invalid transaction format: '{t}'")

        if sign == '+':
            balance += amount
        elif sign == '-':
            if balance - amount >= 0:
                balance -= amount
            # else: skip the withdrawal, balance stays the same
        else:
            raise ValueError(f"Transaction must start with '+' or '-': '{t}'")

        result.append(balance)

    return result
```