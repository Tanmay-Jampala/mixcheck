```python
def indian_format(n: int) -> str:
    """
    Return the integer `n` formatted with Indian style commas.
    The last three digits form a group, and the preceding digits are grouped
    in pairs. Numbers less than 1000 are returned unchanged.
    """
    if n < 0:
        raise ValueError("n must be non‑negative")

    s = str(n)
    if len(s) <= 3:
        return s

    last3 = s[-3:]
    rest = s[:-3]

    # Group the rest in pairs from the right
    groups = []
    i = len(rest)
    while i > 0:
        start = max(0, i - 2)
        groups.append(rest[start:i])
        i -= 2
    groups.reverse()

    return ",".join(groups) + "," + last3
```