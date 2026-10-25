```python
def running_balance(transactions, starting_balance=0):
    balance = starting_balance
    result = []

    for tx in transactions:
        amount = int(tx)
        
        # Check if withdrawal makes balance negative
        if amount < 0 and (balance + amount) < 0:
            # Skip the transaction, balance remains same, but add current balance to result
            result.append(balance)
        else:
            balance += amount
            result.append(balance)
            
    return result
```