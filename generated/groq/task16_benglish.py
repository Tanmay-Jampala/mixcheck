```python
def indian_format(n: int) -> str:
    """Return the Indian style comma formatted string for a non‑negative integer."""
    s = str(n)
    if len(s) <= 3:
        return s

    # Last three digits stay together
    last_three = s[-3:]
    rest = s[:-3]

    # Split the remaining part into groups of two digits from the right
    groups = []
    while len(rest) > 2:
        groups.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        groups.append(rest)

    # Build the final string
    return ','.join(reversed(groups) + [last_three])
```