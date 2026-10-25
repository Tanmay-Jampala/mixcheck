```python
def compress(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + (str(count) if count > 1 else ""))
            count = 1

    return "".join(compressed)
```