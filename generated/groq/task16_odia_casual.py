```python
def indian_format(n: int) -> str:
    """
    Return the Indian‑style comma formatted string for a non‑negative integer.
    Example: 12345678 -> '1,23,45,678'
    Numbers < 1000 are returned unchanged.
    """
    if n < 0:
        raise ValueError("Only non‑negative numbers are allowed")
    s = str(n)
    if len(s) <= 3:
        return s

    # last three digits stay together
    last_three = s[-3:]
    rest = s[:-3]

    # split the remaining part into groups of two digits from the right
    groups = []
    while len(rest) > 2:
        groups.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        groups.append(rest)

    # combine groups in correct order
    indian_part = ','.join(reversed(groups))
    return f"{indian_part},{last_three}"
```