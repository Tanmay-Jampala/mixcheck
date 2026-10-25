```python
def indian_format(n: int) -> str:
    """
    Return the Indian style comma separated representation of a non‑negative integer.
    Example: indian_format(1234567) -> "12,34,567"
    """
    if n < 0:
        raise ValueError("Only non‑negative integers are allowed")
    s = str(n)
    if len(s) <= 3:
        return s

    # Split the last three digits
    last_three = s[-3:]
    prefix = s[:-3]

    # Group the remaining prefix in pairs from the right
    groups = []
    while len(prefix) > 2:
        groups.append(prefix[-2:])
        prefix = prefix[:-2]
    if prefix:
        groups.append(prefix)   # the left‑most group (may be 1 or 2 digits)

    # Assemble the final string
    return ','.join(reversed(groups) + [last_three])
```