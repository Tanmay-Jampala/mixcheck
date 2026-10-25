```python
def indian_format(n: int) -> str:
    s = str(n)
    if len(s) <= 3:
        return s
    last_three = s[-3:]
    remaining = s[:-3]
    groups = []
    for i in range(len(remaining), 0, -2):
        start = max(0, i - 2)
        groups.insert(0, remaining[start:i])
    return ",".join(groups) + "," + last_three
```