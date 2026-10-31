Here’s a compact, well‑documented implementation that follows the exact rules you described:

```python
import re

def valid_mobile(number: str) -> bool:
    """
    Validate an Indian mobile number.

    Rules
    -----
    1. All whitespace characters are ignored.
    2. An optional leading country code “+91” or a leading “0” is stripped.
    3. After stripping, the remaining string must consist of exactly 10 digits.
    4. The first digit of those 10 digits must be 6, 7, 8 or 9.

    Parameters
    ----------
    number: str
        The phone number to validate. It may contain spaces, a leading “+91”,
        or a leading “0”.

    Returns
    -------
    bool
        True if the string satisfies the Indian mobile‑number format,
        False otherwise.

    Examples
    --------
    >>> valid_mobile("  +91 98765 43210 ")
    True
    >>> valid_mobile("09876543210")
    True
    >>> valid_mobile("9876543210")
    True
    >>> valid_mobile("1234567890")
    False
    >>> valid_mobile("+9198765432100")   # 11 digits after +91
    False
    """
    # 1. Remove *all* whitespace (spaces, tabs, newlines, etc.)
    cleaned = re.sub(r"\s+", "", number)

    # 2. Strip optional leading +91 or 0
    if cleaned.startswith("+91"):
        cleaned = cleaned[3:]          # drop the "+91"
    elif cleaned.startswith("0"):
        cleaned = cleaned[1:]          # drop the leading zero

    # 3. At this point we must have exactly 10 digits
    if not re.fullmatch(r"\d{10}", cleaned):
        return False

    # 4. First digit must be 6‑9
    return cleaned[0] in "6789"
```

### How it works
| Step | What we do | Why |
|------|------------|-----|
| **Remove whitespace** | `re.sub(r"\s+", "", number)` | Users often type numbers with spaces for readability. |
| **Strip prefix** | `+91` → drop first 3 chars; `0` → drop first char | Handles the two common ways Indian numbers are written. |
| **Exact‑length check** | `re.fullmatch(r"\d{10}", cleaned)` | Guarantees we have *only* digits and exactly ten of them. |
| **First‑digit check** | `cleaned[0] in "6789"` | Indian mobile numbers start with 6‑9. |

The function returns a simple Boolean, making it easy to plug into validation pipelines, form handling, or unit tests.