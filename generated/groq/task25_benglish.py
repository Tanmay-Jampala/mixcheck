```python
def running_balance(transactions, start_balance):
    balances = []
    balance = start_balance
    for t in transactions:
        amount = int(t)
        # Check if withdrawal would make balance negative
        if amount < 0 and balance + amount < 0:
            # skip transaction, keep balance unchanged
            balances.append(balance)
            continue
        balance += amount
        balances.append(balance)
    return balances
```