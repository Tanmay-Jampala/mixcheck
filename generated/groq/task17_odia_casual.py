```python
import re

def valid_mobile(number: str) -> bool:
    # remove all whitespace
    number = re.sub(r'\s+', '', number)

    # strip leading country code or trunk prefix
    if number.startswith('+91'):
        number = number[3:]
    elif number.startswith('0'):
        number = number[1:]

    # must be exactly 10 digits and start with 6,7,8 or 9
    return len(number) == 10 and number.isdigit() and number[0] in '6789'
```