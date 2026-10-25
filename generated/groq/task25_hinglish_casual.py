```python
def running_balance(transactions, start_balance):
    """
    Calculate the running balance after each transaction.

    Parameters
    ----------
    transactions : list of str
        Each element is a string like "+500" or "-200".
    start_balance : int or float
        The initial balance before any transaction.

    Returns
    -------
    list
        Balance after each transaction. If a withdrawal would make the
        balance drop below zero, that transaction is ignored (balance
        stays the same) but the unchanged balance is still recorded.
    """
    balances = []
    balance = start_balance

    for txn in transactions:
        # Convert the string transaction to a numeric value
        try:
            amount = int(txn) if '.' not in txn else float(txn)
        except ValueError:
            raise ValueError(f"Invalid transaction format: {txn}")

        # Check for withdrawal that would go below zero
        if amount < 0 and balance + amount < 0:
            # Skip the transaction – balance stays the same
            balances.append(balance)
            continue

        # Apply the transaction
        balance += amount
        balances.append(balance)

    return balances


# Example usage
if __name__ == "__main__":
    txns = ["+500", "-200", "-400", "-100", "+300"]
    start = 250
    print(running_balance(txns, start))
    # Output: [750, 550, 550, 450, 750]
```

**Explanation**

1. **Parsing** – Each transaction string is converted to an integer (or float if it contains a decimal point).  
2. **Withdrawal check** – If the amount is negative and applying it would make the balance drop below zero, the transaction is ignored; the current balance is appended to the result list unchanged.  
3. **Apply transaction** – Otherwise the amount is added to the balance and the new balance is recorded.  

The function finally returns a list containing the balance after every transaction, respecting the “no‑overdraft” rule.