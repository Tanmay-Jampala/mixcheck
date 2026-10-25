```python
def indian_format(num):
    """
    Return the Indian‑style comma formatted string for a non‑negative integer.
    Example:
        0          -> "0"
        999        -> "999"
        1000       -> "1,000"
        12345      -> "12,345"
        1234567    -> "12,34,567"
    """
    if not isinstance(num, int) or num < 0:
        raise ValueError("num must be a non‑negative integer")

    s = str(num)
    if len(s) <= 3:
        return s

    # Last three digits stay together
    last_three = s[-3:]
    rest = s[:-3]

    # Group the remaining digits in pairs from the right
    pairs = []
    while len(rest) > 2:
        pairs.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        pairs.append(rest)          # the left‑most group (1 or 2 digits)

    # Assemble: left‑most group first, then pairs reversed, then last three
    formatted = ','.join(reversed(pairs) + [last_three])
    return formatted
```