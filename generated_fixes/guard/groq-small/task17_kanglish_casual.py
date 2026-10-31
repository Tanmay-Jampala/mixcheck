```python
def valid_mobile(number: str) -> bool:
    """
    Validate an Indian mobile number.

    Rules:
    - Remove all spaces.
    - Optionally remove a leading '+91' or '0'.
    - After removal, the string must contain exactly 10 digits.
    - The first digit must be 6, 7, 8, or 9.
    """
    # Remove all spaces
    num = number.replace(" ", "")

    # Remove leading country code or zero
    if num.startswith("+91"):
        num = num[3:]
    elif num.startswith("0"):
        num = num[1:]

    # Must be exactly 10 digits
    if len(num) != 10 or not num.isdigit():
        return False

    # First digit must be 6, 7, 8, or 9
    return num[0] in "6789"
```