```python
def running_balance(transactions, start):
    balance = start
    result = []
    for t in transactions:
        amount = int(t)
        if balance + amount >= 0:
            balance += amount
        result.append(balance)
    return result
```