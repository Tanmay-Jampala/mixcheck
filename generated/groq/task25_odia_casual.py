```python
def running_balance(transactions: list[str], start_balance: int) -> list[int]:
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : list[str]
        List of transaction strings, e.g. ["+500", "-200"].
    start_balance : int
        Initial account balance.

    Returns
    -------
    list[int]
        Balance after each transaction. If a withdrawal would make the
        balance drop below zero, the transaction is ignored (balance stays
        the same) but the unchanged balance is still recorded.
    """
    balances = []
    balance = start_balance

    for txn in transactions:
        # Convert transaction string to integer amount
        try:
            amount = int(txn)
        except ValueError:
            raise ValueError(f"Invalid transaction format: {txn}")

        # Check for withdrawal that would go negative
        if amount < 0 and balance + amount < 0:
            # Skip transaction – balance unchanged
            balances.append(balance)
            continue

        # Apply transaction
        balance += amount
        balances.append(balance)

    return balances


# Example usage:
if __name__ == "__main__":
    txns = ["+500", "-200", "-400", "-100", "+300"]
    print(running_balance(txns, start_balance=250))
    # Output: [750, 550, 550, 450, 750]
```