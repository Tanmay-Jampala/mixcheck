```python
def indian_format(n):
    if n < 0:
        n = abs(n)
    s = str(n)
    if len(s) <= 3:
        return s
    
    last_three = s[-3:]
    other_digits = s[:-3]
    
    res = ""
    while len(other_digits) > 0:
        res = other_digits[-2:] + "," + res
        other_digits = other_digits[:-2]
        
    return res + last_three
```