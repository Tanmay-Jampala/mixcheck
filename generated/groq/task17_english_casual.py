```python
import re

def valid_mobile(number: str) -> bool:
    """
    Validate an Indian mobile number.

    Rules:
    - Remove all whitespace.
    - Optional leading '+91' or '0' is stripped.
    - After stripping, exactly 10 digits must remain.
    - The first digit must be 6, 7, 8, or 9.
    """
    # 1. Remove all whitespace characters
    num = re.sub(r"\s+", "", number)

    # 2. Strip optional country code / leading zero
    if num.startswith("+91"):
        num = num[3:]
    elif num.startswith("0"):
        num = num[1:]

    # 3. Must be exactly 10 digits
    if not re.fullmatch(r"\d{10}", num):
        return False

    # 4. First digit must be 6‑9
    return num[0] in "6789"
```