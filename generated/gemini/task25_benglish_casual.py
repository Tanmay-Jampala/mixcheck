```python
def running_balance(transactions, starting_balance=0):
    balance = starting_balance
    result = []

    for tx in transactions:
        amount = int(tx)

        if amount < 0:
            if balance + amount >= 0:
                balance += amount
        else:
            balance += amount

        result.append(balance)

    return result
```