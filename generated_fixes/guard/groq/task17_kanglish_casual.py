```python
def valid_mobile(number: str) -> bool:
    """
    Validate an Indian mobile number.

    Rules:
    1. Remove all spaces.
    2. Strip a leading '+91' or a leading '0' if present.
    3. The remaining string must be exactly 10 digits.
    4. The first digit must be 6, 7, 8 or 9.

    Returns:
        True if the number satisfies all rules, otherwise False.
    """
    # 1. Remove spaces
    num = number.replace(" ", "")

    # 2. Strip country code or leading zero
    if num.startswith("+91"):
        num = num[3:]
    elif num.startswith("0"):
        num = num[1:]

    # 3. Check length and digit-only
    if len(num) != 10 or not num.isdigit():
        return False

    # 4. First digit must be 6,7,8,9
    return num[0] in "6789"
```