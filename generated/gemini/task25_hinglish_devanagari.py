```python
def running_balance(transactions, starting_balance):
    balance = starting_balance
    result = []
    for tx in transactions:
        amount = int(tx)
        if balance + amount >= 0:
            balance += amount
        result.append(balance)
    return result
```