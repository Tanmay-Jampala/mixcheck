**Python function – `running_balance`**

```python
from typing import List

def running_balance(transactions: List[str], start: int) -> List[int]:
    """
    Compute the running balance after each transaction.

    Parameters
    ----------
    transactions : List[str]
        List of transaction strings, e.g. ["+500", "-200", "-800"].
        Each string must start with '+' or '-' followed by an integer.
    start : int
        The starting balance.

    Returns
    -------
    List[int]
        A list of balances – one entry per transaction.  
        If a withdrawal would bring the balance below zero, that
        transaction is *skipped*: the balance stays unchanged but
        the unchanged value is still appended to the result list.

    Examples
    --------
    >>> running_balance(["+500", "-200", "-800", "+300"], 1000)
    [1500, 1300, 1300, 1600]

    >>> running_balance(["-1200", "+200"], 1000)
    [1000, 1200]   # first withdrawal skipped, second added
    """
    balances = []
    balance = start

    for tx in transactions:
        # Basic validation – raise ValueError if format is wrong
        if not tx or tx[0] not in ('+', '-'):
            raise ValueError(f"Invalid transaction format: {tx!r}")

        amount = int(tx)          # e.g. "+500" -> 500, "-200" -> -200

        # If it's a withdrawal that would make balance negative, skip it
        if amount < 0 and balance + amount < 0:
            # keep balance unchanged
            balances.append(balance)
            continue

        # Apply the transaction
        balance += amount
        balances.append(balance)

    return balances
```

### How it works

1. **Parse each transaction** – the string is converted to an integer (`int(tx)`), which automatically handles the leading `+` or `-`.
2. **Check for overdraft** – if the transaction is a withdrawal (`amount < 0`) and applying it would make the balance negative, the transaction is *skipped*.  
   The balance stays the same, but we still append the unchanged balance to the result list.
3. **Apply the transaction** – otherwise, add the amount to the current balance and append the new balance.

Feel free to drop this function into your project and call it with any list of transaction strings and a starting balance.