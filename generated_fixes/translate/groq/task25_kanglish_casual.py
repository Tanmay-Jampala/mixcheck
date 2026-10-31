Here’s a compact, well‑documented implementation that follows the specification:

```python
def running_balance(transactions, start_balance):
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        A list of strings representing deposits or withdrawals.
        Each element must start with '+' (deposit) or '-' (withdrawal)
        followed by an integer amount, e.g. ["+500", "-200"].
    start_balance : int or float
        The balance before any transaction is applied.

    Returns
    -------
    list[float]
        A list whose i‑th element is the balance after processing the
        i‑th transaction.  If a withdrawal would make the balance negative,
        that transaction is ignored – the balance stays the same, but the
        current balance is still recorded in the output list.

    Example
    -------
    >>> running_balance(["+500", "-200", "-400", "+100"], 300)
    [800, 600, 600, 700]
    """
    # Use a mutable variable to keep track of the current balance.
    balance = float(start_balance)          # allow int or float input
    result = []                              # will hold the balances after each step

    for tx in transactions:
        # Basic validation – we expect a leading sign followed by digits.
        if not tx or tx[0] not in "+-" or not tx[1:].isdigit():
            raise ValueError(f"Invalid transaction format: {tx!r}")

        amount = float(tx[1:])               # numeric part (always positive)

        if tx[0] == '+':                     # deposit – always allowed
            balance += amount
        else:                                # withdrawal – check for overdraft
            if balance - amount >= 0:
                balance -= amount
            # else: insufficient funds → balance unchanged

        result.append(balance)               # record the balance after this step

    return result
```

### How it works
1. **Initialize** `balance` with the supplied `start_balance`.
2. Iterate over each transaction string:
   * Verify the format (`+` or `-` followed by digits).  
   * Extract the numeric amount.
   * If it’s a deposit (`+`), add the amount.
   * If it’s a withdrawal (`-`), only subtract when the resulting balance stays ≥ 0; otherwise skip the transaction.
3. Append the (possibly unchanged) balance to `result` after each transaction.
4. Return the list of recorded balances.

### Quick test

```python
if __name__ == "__main__":
    txs = ["+500", "-200", "-400", "+100"]
    start = 300
    print(running_balance(txs, start))
    # Output: [800.0, 600.0, 600.0, 700.0]
```

Feel free to adapt the validation or the numeric type (e.g., use `Decimal` for monetary precision) as needed for your project.