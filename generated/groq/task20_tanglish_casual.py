```python
def compress(s: str) -> str:
    if not s:
        return ""
    res = []
    prev = s[0]
    cnt = 1
    for ch in s[1:]:
        if ch == prev:
            cnt += 1
        else:
            res.append(prev + (str(cnt) if cnt > 1 else ""))
            prev, cnt = ch, 1
    res.append(prev + (str(cnt) if cnt > 1 else ""))
    return "".join(res)
```