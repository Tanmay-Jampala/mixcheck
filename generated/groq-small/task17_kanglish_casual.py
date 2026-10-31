```python
def valid_mobile(number: str) -> bool:
    """
    Check whether a string is a valid Indian mobile number.

    Rules applied (after stripping all spaces):
    1. Optional leading prefix: '+91' or a single '0' (both removed if present).
    2. Remaining part must be exactly 10 digits.
    3. The first digit of the 10‑digit part must be 6, 7, 8 or 9.

    Parameters
    ----------
    number : str
        The phone number string to validate.

    Returns
    -------
    bool
        True if the string satisfies all the above rules, False otherwise.
    """
    # 1. Remove all spaces
    s = number.replace(' ', '')

    # 2. Strip optional prefix
    if s.startswith('+91'):
        s = s[3:]
    elif s.startswith('0'):
        s = s[1:]

    # 3. Must be exactly 10 digits
    if len(s) != 10 or not s.isdigit():
        return False

    # 4. First digit must be 6,7,8 or 9
    return s[0] in '6789'


# ---- Example usage ----
if __name__ == "__main__":
    test_numbers = [
        "9876543210",          # valid
        "+91 9876543210",      # valid
        "09876543210",         # valid
        "  9876543210  ",      # valid (spaces trimmed)
        "1234567890",          # invalid (starts with 1)
        "+919876543210",       # valid
        "+91 98765 43210",     # valid
        "987654321",           # invalid (9 digits)
        "98765432101",         # invalid (11 digits)
        "+91 987654321a",      # invalid (non‑digit)
    ]

    for num in test_numbers:
        print(f"{num!r:20} -> {valid_mobile(num)}")
```

**Explanation of the logic**

1. **Remove spaces** – `replace(' ', '')` ensures that any whitespace inside the string is ignored.
2. **Optional prefix** –  
   * If the string starts with `+91`, drop the first three characters.  
   * Else if it starts with a single `0`, drop that character.  
   This leaves only the core 10‑digit number (if present).
3. **Length & digit check** – The remaining string must be exactly 10 characters long and all of them must be digits (`s.isdigit()`).
4. **First‑digit rule** – The first digit must belong to the set `{6,7,8,9}`.

If all checks pass, the function returns `True`; otherwise it returns `False`.