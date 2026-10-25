```python
def caesar_shift(text, k):
    """Shift each English letter in `text` by `k` positions.
    
    Parameters
    ----------
    text : str
        The input string.
    k : int
        The shift amount (can be negative or larger than 26).
    
    Returns
    -------
    str
        The Caesar‑shifted string.
    """
    k %= 26  # normalize shift
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # shift lowercase letters
            offset = ord('a')
            shifted = chr(offset + (ord(ch) - offset + k) % 26)
            result.append(shifted)
        elif 'A' <= ch <= 'Z':
            # shift uppercase letters
            offset = ord('A')
            shifted = chr(offset + (ord(ch) - offset + k) % 26)
            result.append(shifted)
        else:
            # non‑letters remain unchanged
            result.append(ch)

    return ''.join(result)
```