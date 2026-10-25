```python
def running_balance(transactions, starting_balance):
    balance = starting_balance
    result = []
    for tx in transactions:
        amount = int(tx)
        if amount < 0 and balance + amount < 0:
            result.append(balance)
        else:
            balance += amount
            result.append(balance)
    return result
```