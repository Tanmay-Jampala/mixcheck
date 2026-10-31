```python
import re


def valid_mobile(number: str) -> bool:
    if not isinstance(number, str):
        return False
    # All spaces remove maadu
    clean_num = number.replace(" ", "")

    # Shuruwalli +91 athava 0 irodanna remove maadu
    if clean_num.startswith("+91"):
        clean_num = clean_num[3:]
    elif clean_num.startswith("0"):
        clean_num = clean_num[1:]

    # Aamele sariyagi 10 digits iddu, 6, 7, 8, 9 ninda shuru agbeku
    pattern = r"^[6-9]\d{9}$"

    return bool(re.match(pattern, clean_num))
```