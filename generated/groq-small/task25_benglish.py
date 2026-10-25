```python
def running_balance(transactions, start_balance):
    balances = []
    balance = start_balance
    for t in transactions:
        amount = int(t)          # handles "+500" or "-200"
        new_balance = balance + amount
        if new_balance < 0:      # skip withdrawal that would go negative
            new_balance = balance
        balance = new_balance
        balances.append(balance)
    return balances
```