```python
def running_balance(starting_balance, transactions):
    balance = starting_balance
    result = []

    for tx in transactions:
        amount = int(tx)

        # Withdrawal (minus) idru, balance zero kinta kami agta idre adann skip maadu
        if amount < 0 and (balance + amount) < 0:
            result.append(balance)
            continue

        balance += amount
        result.append(balance)

    return result
```