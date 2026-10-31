```python
import re


def valid_mobile(phone_str):
    # Spaces tegeyirodu
    clean_str = phone_str.replace(" ", "")

    # Shuruvalia +91 athava 0 anna tegeyirodu
    if clean_str.startswith("+91"):
        clean_str = clean_str[3:]
    elif clean_str.startswith("0"):
        clean_str = clean_str[1:]

    # 10 digits iddu, 6, 7, 8, 9 ninda shuru agutteva anta check madoke regex
    pattern = r"^[6-9]\d{9}$"

    return bool(re.match(pattern, clean_str))
```