```python
def valid_mobile(number: str) -> bool:
    # Remove all spaces
    num = number.replace(' ', '')

    # Remove leading country code or zero
    if num.startswith('+91'):
        num = num[3:]
    elif num.startswith('0'):
        num = num[1:]

    # Check for exactly 10 digits and valid starting digit
    return len(num) == 10 and num.isdigit() and num[0] in '6789'
```