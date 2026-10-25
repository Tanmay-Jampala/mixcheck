```python
import re


def valid_mobile(s):
    if not isinstance(s, str):
        return False
    s = s.replace(" ", "")
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]
    return bool(re.match(r"^[6-7-8-9]\d{9}$", s))
```