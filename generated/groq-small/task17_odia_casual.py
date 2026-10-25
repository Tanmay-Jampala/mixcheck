```python
def is_valid_mobile(number: str) -> bool:
    # Remove all spaces
    number = number.replace(' ', '')

    # Remove leading +91 or 0
    if number.startswith('+91'):
        number = number[3:]
    elif number.startswith('0'):
        number = number[1:]

    # Check length, digits, and starting digit
    return (
        len(number) == 10
        and number.isdigit()
        and number[0] in '6789'
    )
```