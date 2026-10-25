```python
import re


def valid_mobile(s: str) -> bool:
    if not isinstance(s, str):
        return False

    # 1. Samast space hatao
    s = s.replace(" ", "")

    # 2. Aarambha re +91 ba 0 thile hatao (kebala thare)
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]

    # 3. Check kara je thik 10 ta digit achi ki nahi ebong pratham digit 6, 7, 8 ba 9 kideki
    pattern = r"^[6-9]\d{9}$"

    return bool(re.match(pattern, s))
```