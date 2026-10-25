```python
def indian_format(n: int) -> str:
    """
    Format a non‑negative integer using the Indian numbering system.
    Example: 1234567 -> "12,34,567"
    """
    s = str(n)
    if len(s) <= 3:
        return s

    # Last three digits
    last3 = s[-3:]
    # Remaining digits
    rest = s[:-3]

    # Group the remaining digits in pairs from the right
    pairs = []
    while rest:
        pairs.append(rest[-2:])
        rest = rest[:-2]
    # Join the pairs with commas and add the last three digits
    return ",".join(reversed(pairs)) + "," + last3
```