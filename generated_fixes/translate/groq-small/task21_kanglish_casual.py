```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift every English letter in *text* forward by *k* positions.
    The shift wraps around after 'z' to 'a' (or 'Z' to 'A').
    Non‑letter characters are left unchanged.

    Parameters
    ----------
    text : str
        The input string to be shifted.
    k : int
        The number of positions to shift.  Can be negative.

    Returns
    -------
    str
        The Caesar‑shifted string.
    """
    result = []

    # Normalise k to the range 0–25
    k = k % 26

    for ch in text:
        if 'a' <= ch <= 'z':
            # Shift lowercase letters
            shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= ch <= 'Z':
            # Shift uppercase letters
            shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        else:
            # Leave non‑letters unchanged
            result.append(ch)

    return ''.join(result)
```

**Example**

```python
print(caesar_shift("Hello, World!", 3))
# Output: "Khoor, Zruog!"
```

The function works for any integer `k` (positive, negative, or zero) and preserves the case of letters while leaving all other characters untouched.