```python
import re

def valid_mobile(s: str) -> bool:
    # Remove all whitespace characters
    s = re.sub(r'\s+', '', s)

    # Remove leading +91 or 0 if present
    if s.startswith('+91'):
        s = s[3:]
    elif s.startswith('0'):
        s = s[1:]

    # After stripping prefix, the string must be exactly 10 digits
    if not re.fullmatch(r'\d{10}', s):
        return False

    # First digit must be 6, 7, 8 or 9
    return s[0] in '6789'
```