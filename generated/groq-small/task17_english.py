```python
def valid_mobile(number: str) -> bool:
    # Remove all spaces
    num = number.replace(' ', '')

    # Remove prefix if present
    if num.startswith('+91'):
        num = num[3:]
    elif num.startswith('0'):
        num = num[1:]

    # Check that the remaining string is exactly 10 digits
    if len(num) != 10 or not num.isdigit():
        return False

    # First digit must be 6, 7, 8, or 9
    return num[0] in '6789'
```