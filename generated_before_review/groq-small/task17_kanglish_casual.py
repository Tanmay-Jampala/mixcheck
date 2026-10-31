**Python function – `valid_mobile`**

```python
import re

def valid_mobile(number: str) -> bool:
    """
    Return True if *number* is a valid Indian mobile number, otherwise False.

    Rules applied (in order):
    1. Strip all whitespace characters.
    2. Remove a leading country code `+91` or a leading zero `0` if present.
    3. After the optional prefix, the remaining string must contain **exactly 10 digits**.
    4. The first digit of the 10‑digit part must be 6, 7, 8 or 9.
    """
    # 1. Remove all whitespace
    num = re.sub(r'\s+', '', number)

    # 2. Strip leading +91 or 0
    if num.startswith('+91'):
        num = num[3:]
    elif num.startswith('0'):
        num = num[1:]

    # 3. Must be 10 digits
    if not re.fullmatch(r'\d{10}', num):
        return False

    # 4. First digit must be 6‑9
    return num[0] in '6789'


# ------------------------------------------------------------------
# Example usage
# ------------------------------------------------------------------
if __name__ == "__main__":
    test_numbers = [
        "9876543210",          # valid
        "+91 9876543210",      # valid
        "09876543210",         # valid
        "  9876543210  ",      # valid (spaces trimmed)
        "1234567890",          # invalid – starts with 1
        "+919876543210",       # valid
        "+91 98765 43210",     # valid (spaces inside)
        "987654321",           # invalid – only 9 digits
        "98765432101",         # invalid – 11 digits
        "+91 987654321a",      # invalid – contains letter
    ]

    for n in test_numbers:
        print(f"{n!r:20} -> {valid_mobile(n)}")
```

### How it works

| Step | What happens | Why |
|------|--------------|-----|
| 1 | `re.sub(r'\s+', '', number)` | Removes **all** whitespace (spaces, tabs, newlines). |
| 2 | Strip `+91` or `0` | Indian numbers may be written with the country code or a leading zero. |
| 3 | `re.fullmatch(r'\d{10}', num)` | Ensures the remaining string is **exactly** 10 digits. |
| 4 | `num[0] in '6789'` | Valid Indian mobile numbers start with 6, 7, 8 or 9. |

The function returns a boolean (`True` for a valid number, `False` otherwise). It is lightweight, uses only the standard library, and can be dropped into any project that needs to validate Indian mobile numbers.