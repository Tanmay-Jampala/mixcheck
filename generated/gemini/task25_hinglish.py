```python
def running_balance(transactions, starting_balance):
    balance = starting_balance
    result = []
    
    for tx in transactions:
        amount = int(tx)
        # Agar withdrawal hai aur balance se zyada hai, to skip karo
        if amount < 0 and balance + amount < 0:
            result.append(balance)
        else:
            balance += amount
            result.append(balance)
            
    return result
```