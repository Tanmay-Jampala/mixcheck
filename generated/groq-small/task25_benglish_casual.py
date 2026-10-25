```python
def running_balance(transactions, starting_balance):
    """
    Calculate the running balance after each transaction.

    Parameters
    ----------
    transactions : list of str
        Each transaction is a string like "+500" or "-200".
    starting_balance : int
        The balance before any transaction.

    Returns
    -------
    list of int
        The balance after each transaction.  
        If a withdrawal would make the balance negative, that
        transaction is skipped (balance stays the same) but the
        unchanged balance is still added to the result list.
    """
    balances = []
    balance = starting_balance

    for t in transactions:
        amount = int(t)          # works for "+500" and "-200"
        new_balance = balance + amount

        # Skip withdrawal that would go below zero
        if amount < 0 and new_balance < 0:
            new_balance = balance

        balances.append(new_balance)
        balance = new_balance

    return balances
```