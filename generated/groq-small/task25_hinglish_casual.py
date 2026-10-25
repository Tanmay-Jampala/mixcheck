```python
def running_balance(transactions, start_balance):
    """
    Calculate the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        List of transaction strings, e.g. ["+500", "-200", "+300"].
    start_balance : int
        The balance before any transaction.

    Returns
    -------
    list[int]
        Balance after each transaction.  If a withdrawal would make the
        balance negative, that transaction is ignored (balance stays the
        same) but the unchanged balance is still appended to the list.
    """
    balance = start_balance
    result = []

    for t in transactions:
        t = t.strip()          # remove any accidental whitespace
        if not t:
            continue           # skip empty strings

        sign = t[0]
        try:
            amount = int(t[1:])
        except ValueError:
            raise ValueError(f"Invalid transaction format: '{t}'")

        if sign == '+':
            balance += amount
        elif sign == '-':
            # Skip if it would go below zero
            if balance - amount < 0:
                # balance unchanged
                pass
            else:
                balance -= amount
        else:
            raise ValueError(f"Transaction must start with '+' or '-': '{t}'")

        result.append(balance)

    return result
```

**Example**

```python
>>> running_balance(["+500", "-200", "-400", "+300"], 100)
[600, 400, 400, 700]
```

The third transaction (`-400`) would bring the balance below zero, so it is ignored, but the unchanged balance `400` is still added to the result list.