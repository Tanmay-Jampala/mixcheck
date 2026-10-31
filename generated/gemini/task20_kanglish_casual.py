```python
def compress(s):
    if not s:
        return ""
    res = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 1
        while i + 1 < len(s) and s[i + 1] == char:
            count += 1
            i += 1
        res.append(char + (str(count) if count > 1 else ""))
        i += 1
    return "".join(res)
```