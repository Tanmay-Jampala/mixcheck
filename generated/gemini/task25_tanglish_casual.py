```python
def calculate_running_balance(starting_balance, transactions):
    balance = starting_balance
    result = [balance]

    for tx in transactions:
        amount = int(tx)
        if balance + amount < 0:
            result.append(balance)
        else:
            balance += amount
            result.append(balance)

    return result
```