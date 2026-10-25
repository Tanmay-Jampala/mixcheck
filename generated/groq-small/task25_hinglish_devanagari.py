```python
def running_balance(transactions, start_balance):
    balances = []
    balance = start_balance
    for t in transactions:
        amount = int(t)
        if amount < 0 and balance + amount < 0:
            balances.append(balance)          # skip withdrawal
        else:
            balance += amount
            balances.append(balance)
    return balances
```