```python
def indian_format(n: int) -> str:
    """
    Return the Indian-style comma formatted string for a non‑negative integer.
    - Numbers < 1000 are returned unchanged.
    - For larger numbers, the last three digits form a group,
      and the preceding digits are grouped in pairs of two.
    """
    if n < 0:
        raise ValueError("Only non‑negative numbers are allowed")
    s = str(n)
    if len(s) <= 3:
        return s

    # Last three digits
    last_three = s[-3:]
    # Remaining part to be grouped in pairs
    prefix = s[:-3]

    # Build groups of two from right to left
    groups = []
    while prefix:
        groups.append(prefix[-2:])
        prefix = prefix[:-2]

    # Combine groups with commas
    formatted = ",".join(reversed(groups)) + "," + last_three
    return formatted
```