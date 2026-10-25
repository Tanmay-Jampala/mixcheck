```python
import re


def valid_mobile(s: str) -> bool:
    if not isinstance(s, str):
        return False
    s = s.replace(" ", "")
    s = re.sub(r"^(\+91|0)", "", s)
    return bool(re.fullmatch(r"[6-9]\d{9}", s))
```