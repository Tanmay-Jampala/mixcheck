```python
def compress(s):
    if not s:
        return ""
    res = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        res.append(s[i] if count == 1 else s[i] + str(count))
        i += 1
    return "".join(res)
```