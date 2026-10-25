```python
def bhai_indian_format(n: int | float) -> str:
    s = str(n)
    if '.' in s:
        int_part, dec_part = s.split('.')
    else:
        int_part, dec_part = s, None

    if len(int_part) <= 3:
        formatted = int_part
    else:
        last_three = int_part[-3:]
        rest = int_part[:-3]
        groups = []
        while len(rest) > 2:
            groups.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            groups.append(rest)
        formatted = ','.join(reversed(groups)) + ',' + last_three

    if dec_part:
        formatted += '.' + dec_part
    return formatted
```