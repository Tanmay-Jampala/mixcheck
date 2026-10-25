```python
def valid_mobile(s: str) -> bool:
    s = s.replace(" ", "")
    
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]
        
    if len(s) == 10 and s.isdigit() and s[0] in "6789":
        return True
    return False
```