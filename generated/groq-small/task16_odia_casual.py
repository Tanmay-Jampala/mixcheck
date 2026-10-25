```python
def indian_format(num: int) -> str:
    """
    Convert a non‑negative integer to a string formatted in the Indian numbering system.
    Example:
        12345678 -> '1,23,45,678'
        1234      -> '1,234'
        999       -> '999'
    """
    s = str(num)

    # Numbers with 3 or fewer digits need no comma
    if len(s) <= 3:
        return s

    # Split the last three digits
    last3 = s[-3:]
    rest = s[:-3]

    # Group the remaining digits in pairs from the right
    groups = []
    while rest:
        groups.append(rest[-2:])
        rest = rest[:-2]
    groups.reverse()

    return ','.join(groups) + ',' + last3
```