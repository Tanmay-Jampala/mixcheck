```python
def indian_format(n: int) -> str:
    """Return the Indian‑style comma formatted string for a non‑negative integer."""
    if n < 0:
        raise ValueError("n must be non‑negative")
    s = str(n)
    if len(s) <= 3:
        return s

    # Split the last three digits
    tail = s[-3:]
    head = s[:-3]

    # Group the remaining digits in pairs from the right
    pairs = []
    while len(head) > 2:
        pairs.append(head[-2:])
        head = head[:-2]
    if head:
        pairs.append(head)

    # Assemble: head groups (reversed) + tail
    return ','.join(reversed(pairs)) + ',' + tail
```