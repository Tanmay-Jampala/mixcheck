**Solution Overview**

We need a function `valid_mobile(s: str) -> bool` that tells whether a given string represents a **valid Indian mobile number**.

The validation rules are:

1. **Ignore any spaces** that may appear anywhere in the string.  
2. **Remove a leading country code** (`+91`) **or** a leading trunk‑prefix (`0`).  
   *Only one of them may be present; if both appear (e.g. `+910...`) we treat it as invalid.*  
3. After the optional prefix is stripped, the remaining part must consist of **exactly 10 digits**.  
4. The **first digit** of those 10 digits must be **6, 7, 8 or 9**.  

If all the above conditions are satisfied the function returns `True`, otherwise `False`.

---

## Implementation

```python
import re

def valid_mobile(number: str) -> bool:
    """
    Validate an Indian mobile number.

    Parameters
    ----------
    number : str
        The phone number as a string. It may contain spaces,
        a leading '+91' country code or a leading '0'.

    Returns
    -------
    bool
        True if the string is a valid Indian mobile number,
        False otherwise.
    """
    # 1️⃣ Remove all whitespace characters (spaces, tabs, newlines …)
    num = re.sub(r'\s+', '', number)

    # 2️⃣ Strip a leading '+91' or a leading '0' (but not both)
    if num.startswith('+91'):
        num = num[3:]          # drop '+91'
    elif num.startswith('0'):
        num = num[1:]          # drop the leading zero

    # 3️⃣ After stripping, the string must be exactly 10 digits
    if not re.fullmatch(r'\d{10}', num):
        return False

    # 4️⃣ First digit must be 6, 7, 8 or 9
    return num[0] in {'6', '7', '8', '9'}
```

### Why this works

| Step | What we do | Reason |
|------|------------|--------|
| **Remove spaces** | `re.sub(r'\s+', '', number)` | Users often paste numbers with spaces (`"  +91  98765 43210 "`). Removing all whitespace normalises the input. |
| **Strip prefix** | `if num.startswith('+91') … elif num.startswith('0') …` | Indian numbers may be written with the country code (`+91`) or with the trunk prefix (`0`). Only one of them is allowed; we drop it so that we are left with the pure 10‑digit subscriber number. |
| **Exact 10 digits** | `re.fullmatch(r'\d{10}', num)` | Guarantees that nothing else (letters, extra digits, punctuation) remains. |
| **First digit check** | `num[0] in {'6','7','8','9'}` | Mobile numbers in India are allocated only in the range 6‑9. Land‑line numbers (starting with 1‑5) are therefore rejected. |

---

## Quick test‑suite

```python
if __name__ == "__main__":
    test_cases = {
        "9876543210": True,
        " 98765 43210 ": True,
        "+91 9876543210": True,
        "+91-9876543210": False,   # hyphen not removed -> invalid
        "0 9876543210": True,
        "091234567890": False,     # after stripping 0 we get 9 digits
        "+919876543210": True,
        "+91 09876543210": False,  # both +91 and leading 0 -> invalid
        "1234567890": False,       # starts with 1
        "987654321": False,        # only 9 digits
        "98765432100": False,      # 11 digits
        "98765a43210": False,      # contains a letter
        "": False,
    }

    for inp, expected in test_cases.items():
        result = valid_mobile(inp)
        print(f"{inp!r:20} → {result} (expected {expected})")
```

Running the script prints:

```
'9876543210'          → True (expected True)
' 98765 43210 '       → True (expected True)
'+91 9876543210'      → True (expected True)
'+91-9876543210'      → False (expected False)
'0 9876543210'        → True (expected True)
'091234567890'        → False (expected False)
'+919876543210'       → True (expected True)
'+91 09876543210'     → False (expected False)
'1234567890'          → False (expected False)
'987654321'           → False (expected False)
'98765432100'         → False (expected False)
'98765a43210'         → False (expected False)
''                    → False (expected False)
```

All test cases behave as intended.

---

### Usage example

```python
>>> valid_mobile("  +91  98765 43210 ")
True
>>> valid_mobile("0123456789")
False   # starts with 0 after stripping -> first digit is 1
>>> valid_mobile("98765 4321")
False   # only 9 digits left
```

Feel free to copy the function into your project; it has **O(n)** time complexity (linear in the length of the input string) and uses only the standard library.