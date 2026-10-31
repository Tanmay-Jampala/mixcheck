```python
def indian_format(n: int) -> str:
    """
    Return the Indian style formatted string for a non‑negative integer.
    Groups: last 3 digits, then groups of 2 digits.
    Numbers less than 1000 are returned unchanged.
    """
    s = str(n)
    if len(s) <= 3:
        return s

    last3 = s[-3:]
    rest = s[:-3]

    groups = []
    while rest:
        groups.append(rest[-2:])
        rest = rest[:-2]
    groups.reverse()

    return ','.join(groups) + ',' + last3
```