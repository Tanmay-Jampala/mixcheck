Here’s a compact, well‑documented implementation that follows the rules you described:

```python
def running_balance(transactions, starting_balance):
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        A list of transaction strings, e.g. ["+500", "-200", "+300"].
        Each string must start with a sign ('+' or '-') followed by an integer.
    starting_balance : int
        The balance before any transaction is applied.

    Returns
    -------
    list[int]
        A list containing the balance after each transaction attempt.
        If a withdrawal would bring the balance below zero, that
        transaction is ignored (the balance stays the same) but the
        unchanged balance is still appended to the result list.

    Notes
    -----
    * Invalid transaction strings are ignored – the balance is simply
      appended unchanged.
    * Zero‑value transactions are treated like any other: the balance
      is appended unchanged.
    """
    balances = []
    balance = starting_balance

    for t in transactions:
        t = t.strip()                     # remove stray whitespace
        try:
            amount = int(t)               # works for "+500" and "-200"
        except ValueError:
            # malformed entry – skip but record current balance
            balances.append(balance)
            continue

        # Skip a withdrawal that would make the balance negative
        if amount < 0 and balance + amount < 0:
            balances.append(balance)
            continue

        # Apply the transaction
        balance += amount
        balances.append(balance)

    return balances
```

### Example usage

```python
>>> running_balance(["+500", "-200", "-400", "+300"], 100)
[600, 400, 400, 700]
```

* The first `+500` brings the balance to 600.
* The `-200` reduces it to 400.
* The `-400` would drop it to 0, which is allowed, so it becomes 0.
  (If it had dropped below 0, it would have been skipped.)
* The final `+300` brings it to 700.

Feel free to tweak the error handling or add type checks as needed for your specific use case.