```python
def calculate_running_balance(transactions, starting_balance=0):
    balance = starting_balance
    balance_list = []

    for tx in transactions:
        amount = int(tx)
        new_balance = balance + amount

        if new_balance < 0:
            balance_list.append(balance)
        else:
            balance = new_balance
            balance_list.append(balance)

    return balance_list
```