```python
def compress_string(s):
    if not s:
        return ""
    res = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        res.append(s[i] + (str(count) if count > 1 else ""))
        i += 1
    return "".join(res)
```