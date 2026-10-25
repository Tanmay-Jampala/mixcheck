```python
def indian_format(n: int) -> str:
    """
    Return the Indian‑style comma formatted string for a non‑negative integer.
    Example: 12345678 -> '1,23,45,678'
    Numbers < 1000 are returned without commas.
    """
    if n < 0:
        raise ValueError("Only non‑negative numbers are allowed")
    s = str(n)
    if len(s) <= 3:
        return s

    # first group of three digits (rightmost)
    tail = s[-3:]
    head = s[:-3]

    # subsequent groups of two digits
    groups = []
    while len(head) > 2:
        groups.append(head[-2:])
        head = head[:-2]
    if head:
        groups.append(head)

    # combine groups in reverse order and add the tail
    return ','.join(reversed(groups)) + ',' + tail
```