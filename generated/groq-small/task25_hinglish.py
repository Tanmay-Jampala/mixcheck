```python
def running_balance(transactions, start_balance):
    balances = []
    current = start_balance
    for t in transactions:
        amount = int(t)
        if amount < 0 and current + amount < 0:
            # skip withdrawal that would make balance negative
            balances.append(current)
        else:
            current += amount
            balances.append(current)
    return balances
```