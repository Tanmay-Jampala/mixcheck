```python
def indian_format(n: int) -> str:
    s = str(n)
    if len(s) <= 3:
        return s

    last3 = s[-3:]
    rest = s[:-3]
    groups = []

    while rest:
        groups.append(rest[-2:])
        rest = rest[:-2]

    return ','.join(reversed(groups)) + ',' + last3
```