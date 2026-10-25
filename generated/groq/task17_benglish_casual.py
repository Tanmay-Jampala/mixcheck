```python
import re

def valid_mobile(number: str) -> bool:
    """
    Validate an Indian mobile number.

    Steps:
    1. Remove all whitespace.
    2. Strip a leading '+91' or '0' if present.
    3. Ensure the remaining string has exactly 10 digits.
    4. The first digit must be 6, 7, 8, or 9.

    Returns:
        True if the string is a valid Indian mobile number, else False.
    """
    # 1. Remove all whitespace characters
    num = re.sub(r'\s+', '', number)

    # 2. Strip leading country code or trunk prefix
    if num.startswith('+91'):
        num = num[3:]
    elif num.startswith('0'):
        num = num[1:]

    # 3. Check length and digit-only content
    if len(num) != 10 or not num.isdigit():
        return False

    # 4. First digit must be 6, 7, 8, or 9
    return num[0] in {'6', '7', '8', '9'}
```