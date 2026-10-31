```python
def running_balance(transactions, start):
    """
    Compute running balances for a list of transactions.

    Parameters
    ----------
    transactions : list of str
        Each element is a string like "+500" (deposit) or "-200" (withdrawal).
    start : int
        Starting balance.

    Returns
    -------
    list of int
        Balance after each successful transaction. Transactions that would
        make the balance negative are ignored.
    """
    balance = start
    result = []

    for txn in transactions:
        txn = txn.strip()
        if not txn:
            continue

        # Determine sign and amount
        sign = txn[0]
        try:
            amount = int(txn[1:])
        except Value‑Error:
            raise ValueError(f"Invalid transaction format: {txn}")

        # Compute tentative new balance
        new_balance = balance + amount if sign == '+' else balance - amount

        # Skip if withdrawal would overdraw the account
        if new_balance < 0:
            continue

        balance = new_balance
        result.append(balance)

    return result
```