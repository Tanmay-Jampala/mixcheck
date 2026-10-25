```python
import re


def valid_mobile(number_str):
    if not isinstance(number_str, str):
        return False

    # 1. सारे spaces हटा दो
    cleaned = number_str.replace(" ", "")

    # 2. "+91" या "0" prefix हटा दो
    if cleaned.startswith("+91"):
        cleaned = cleaned[3:]
    elif cleaned.startswith("0"):
        cleaned = cleaned[1:]

    # 3. Check करो कि बचा हुआ string exactly 10 digits का है और 6, 7, 8, या 9 से शुरू होता है
    if re.fullmatch(r"[6-9]\d{9}", cleaned):
        return True

    return False
```