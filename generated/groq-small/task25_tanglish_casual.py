```python
def running_balance(transactions, starting_balance):
    """
    Calculate the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        List of transaction strings, e.g. ["+500", "-200", "-800"].
    starting_balance : int
        The balance before any transaction.

    Returns
    -------
    list[int]
        The balance after each transaction.  
        If a withdrawal would make the balance negative, that transaction is
        skipped (balance stays the same) but the unchanged balance is still
        appended to the result list.
    """
    balance = starting_balance
    result = []

    for t in transactions:
        # Convert the transaction string to an integer amount
        try:
            amount = int(t)
        except ValueError:
            raise ValueError(f"Invalid transaction format: {t!r}")

        # Check for a withdrawal that would overdraw the account
        if amount < 0 and balance + amount < 0:
            # Skip the transaction but keep the current balance
            result.append(balance)
            continue

        # Apply the transaction
        balance += amount
        result.append(balance)

    return result
```

**Example**

```python
>>> running_balance(["+500", "-200", "-800", "+300"], 1000)
[1500, 1300, 1300, 1600]
```

The third transaction (`-800`) would bring the balance below zero, so it is skipped and the balance remains `1300`. The unchanged balance is still added to the output list.