def running_balance(transactions, starting_balance):
    balances = []
    balance = starting_balance
    for t in transactions:
        if not t:
            balances.append(balance)
            continue
        sign = t[0]
        try:
            amount = int(t[1:])
        except ValueError:
            # If the transaction string is malformed, skip it
            balances.append(balance)
            continue
        if sign == '+':
            balance += amount
        elif sign == '-':
            if balance - amount >= 0:
                balance -= amount
        # Append the balance after this transaction
        balances.append(balance)
    return balances