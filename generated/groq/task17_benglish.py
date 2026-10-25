```python
import re

def valid_mobile(s: str) -> bool:
    """
    Returns True if `s` is a valid Indian mobile number, otherwise False.
    Rules:
        * All whitespace is ignored.
        * Optional leading "+91" or "0" is stripped.
        * The remaining part must be exactly 10 digits.
        * The first digit must be 6, 7, 8 or 9.
    """
    # 1. Remove all whitespace characters
    s = re.sub(r"\s+", "", s)

    # 2. Strip optional country code / leading zero
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]

    # 3. Validate the remaining string
    if len(s) != 10 or not s.isdigit():
        return False
    return s[0] in "6789"
```