```python
def running_balance(transactions, start_balance):
    balance = start_balance
    result = []
    for t in transactions:
        amount = int(t)               # "+500" -> 500, "-200" -> -200
        if balance + amount < 0:      # would go below zero -> skip
            result.append(balance)
            continue
        balance += amount
        result.append(balance)
    return result
```