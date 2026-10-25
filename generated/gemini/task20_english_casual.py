```python
def compress(s: str) -> str:
    if not s:
        return ""
    
    res = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(s[i - 1] + (str(count) if count > 1 else ""))
            count = 1
            
    res.append(s[-1] + (str(count) if count > 1 else ""))
    return "".join(res)
```