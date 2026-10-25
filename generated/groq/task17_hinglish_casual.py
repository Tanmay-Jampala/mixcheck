```python
def valid_mobile(num: str) -> bool:
    # Remove all whitespace characters
    num = "".join(num.split())

    # Remove leading country code (+91) or a leading zero
    if num.startswith("+91"):
        num = num[3:]
    elif num.startswith("0"):
        num = num[1:]

    # After stripping, it must be exactly 10 digits
    if len(num) != 10 or not num.isdigit():
        return False

    # First digit must be 6, 7, 8 or 9
    return num[0] in "6789"
```