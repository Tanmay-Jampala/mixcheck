```python
def valid_mobile(s: str) -> bool:
    # remove all spaces
    s = s.replace(' ', '')

    # strip leading country code or zero
    if s.startswith('+91'):
        s = s[3:]
    elif s.startswith('0'):
        s = s[1:]

    # must be exactly 10 digits and start with 6,7,8 or 9
    return len(s) == 10 and s.isdigit() and s[0] in '6789'
```