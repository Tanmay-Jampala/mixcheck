```python
def indian_format(n: int) -> str:
    if n < 0:
        raise ValueError("Non-negative number matra kodi.")

    s = str(n)
    if len(s) <= 3:
        return s

    last_three = s[-3:]
    other_digits = s[:-3]

    res = []
    while len(other_digits) > 0:
        res.append(other_digits[-2:])
        other_digits = other_digits[:-2]

    res.reverse()
    return ",".join(res) + "," + last_three
```