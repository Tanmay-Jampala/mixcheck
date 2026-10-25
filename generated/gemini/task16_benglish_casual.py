```python
def indian_format(n: int) -> str:
    s = str(n)
    if n < 1000:
        return s

    last_three = s[-3:]
    remaining = s[:-3]

    groups = []
    while len(remaining) > 0:
        groups.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    return ",".join(groups + [last_three])
```