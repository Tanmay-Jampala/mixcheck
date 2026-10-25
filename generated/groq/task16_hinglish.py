```python
def indian_format(n: int) -> str:
    """
    Return the Indian numbering format of a non‑negative integer.
    Example: indian_format(1234567) -> "12,34,567"
    """
    if n < 0:
        raise ValueError("Only non‑negative integers are allowed")
    s = str(n)
    # No commas needed for numbers with 3 or fewer digits
    if len(s) <= 3:
        return s

    # First group: last three digits
    last_three = s[-3:]
    # Remaining part (if any) will be grouped in pairs from the right
    prefix = s[:-3]

    # Build groups of two digits from the right side of the prefix
    groups = []
    while prefix:
        groups.append(prefix[-2:])   # take last two digits
        prefix = prefix[:-2]        # remove them

    # The groups are collected in reverse order, so reverse them back
    groups.reverse()
    return ','.join(groups + [last_three])
```