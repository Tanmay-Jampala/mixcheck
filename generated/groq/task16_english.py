```python
def indian_format(n: int) -> str:
    """Return the Indian‑style comma formatted string for a non‑negative integer."""
    s = str(n)
    if len(s) <= 3:
        return s

    # Last three digits form the final group
    last_three = s[-3:]
    prefix = s[:-3]

    # Split the remaining prefix into groups of two digits from the right
    groups = []
    while len(prefix) > 2:
        groups.append(prefix[-2:])
        prefix = prefix[:-2]
    if prefix:
        groups.append(prefix)

    # Reverse to restore original order and join with commas
    groups.reverse()
    return ','.join(groups + [last_three])
```