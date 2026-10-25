```python
def running_balance(transactions, start_balance):
    """
    Compute running balances.

    Parameters
    ----------
    transactions : list[str]
        List of transaction strings, e.g. "+500", "-200".
    start_balance : int or float
        Initial account balance.

    Returns
    -------
    list[int|float]
        Balance after each transaction. If a withdrawal would make the
        balance drop below zero, the transaction is ignored (balance stays
        the same) but the unchanged balance is still recorded.
    """
    bal = start_balance
    balances = []

    for txn in transactions:
        # Convert transaction string to numeric value
        try:
            amount = int(txn) if isinstance(txn, str) else float(txn)
        except ValueError:
            raise ValueError(f"Invalid transaction format: {txn}")

        # Check for withdrawal that would go negative
        if amount < 0 and bal + amount < 0:
            # Skip the transaction, keep balance unchanged
            balances.append(bal)
            continue

        # Apply transaction
        bal += amount
        balances.append(bal)

    return balances
```