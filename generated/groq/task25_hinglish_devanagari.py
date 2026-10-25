```python
def running_balance(transactions, start_balance):
    balances = []
    balance = start_balance
    for txn in transactions:
        amount = int(txn)               # "+500" -> 500, "-200" -> -200
        # If a withdrawal would make balance negative, skip it
        if amount < 0 and balance + amount < 0:
            balances.append(balance)    # balance unchanged, but recorded
        else:
            balance += amount
            balances.append(balance)
    return balances
```