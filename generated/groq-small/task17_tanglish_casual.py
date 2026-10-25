```python
def valid_mobile(number: str) -> bool:
    # Remove all spaces
    s = number.replace(" ", "")
    
    # Strip leading country code or zero
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]
    
    # Must be exactly 10 digits
    if len(s) != 10 or not s.isdigit():
        return False
    
    # First digit must be 6, 7, 8, or 9
    return s[0] in "6789"
```