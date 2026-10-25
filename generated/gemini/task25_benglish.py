```python
def running_balance(transactions, starting_balance):
    current_balance = starting_balance
    result = []
    
    for tx in transactions:
        amount = int(tx)
        
        # Jodi withdrawal (negative) hoy ebong balance zero er niche chole jay
        if amount < 0 and (current_balance + amount) < 0:
            # Transaction skip hobe, balance same thakbe
            pass
        else:
            current_balance += amount
            
        result.append(current_balance)
        
    return result
```