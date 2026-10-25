```python
def compress(s):
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            count += 1
        
        result.append(s[i])
        if count > 1:
            result.append(str(count))
        i += 1
        
    return "".join(result)
```