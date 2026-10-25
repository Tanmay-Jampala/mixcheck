```python
import re

def valid_mobile(number: str) -> bool:
    # Remove all whitespace characters
    num = re.sub(r'\s+', '', number)

    # Strip country code (+91) or leading zero
    if num.startswith('+91'):
        num = num[3:]
    elif num.startswith('0'):
        num = num[1:]

    # Must be exactly 10 digits and start with 6,7,8 or 9
    return len(num) == 10 and num.isdigit() and num[0] in '6789'
```