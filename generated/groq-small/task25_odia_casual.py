```python
def running_balance(transactions, starting_balance):
    balances = []
    balance = starting_balance
    for t in transactions:
        amt = int(t)                     # e.g., "+500" -> 500, "-200" -> -200
        if amt < 0 and balance + amt < 0:
            # withdrawal would make balance negative – skip it
            balances.append(balance)
        else:
            balance += amt
            balances.append(balance)
    return balances
```