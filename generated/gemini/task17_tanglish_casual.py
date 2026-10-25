```python
import re


def valid_mobile(phone_str: str) -> bool:
    # 1. Remove all spaces
    cleaned = phone_str.replace(" ", "")

    # 2. Remove leading +91 or 0
    if cleaned.startswith("+91"):
        cleaned = cleaned[3:]
    elif cleaned.startswith("0"):
        cleaned = cleaned[1:]

    # 3. Check if it has exactly 10 digits and starts with 6, 7, 8, or 9
    pattern = r"^[6-9]\d{9}$"

    return bool(re.match(pattern, cleaned))
```