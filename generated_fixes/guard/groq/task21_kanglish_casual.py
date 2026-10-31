```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift each English alphabetic character in `text` forward by `k` positions.
    - Wraps around within the alphabet (e.g., 'z' -> 'a', 'Z' -> 'A').
    - Preserves the original case.
    - Non‑alphabetic characters (spaces, digits, punctuation, etc.) are left unchanged.

    Parameters
    ----------
    text : str
        Input string to be transformed.
    k : int
        Number of positions to shift. Can be any integer (positive, negative, or zero).

    Returns
    -------
    str
        The shifted string.
    """
    k = k % 26  # Normalize shift to range [0, 25]
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # Compute shifted position for lowercase letters
            shifted = (ord(ch) - ord('a') + k) % 26 + ord('a')
            result.append(chr(shifted))
        elif 'A' <= ch <= 'Z':
            # Compute shifted position for uppercase letters
            shifted = (ord(ch) - ord('A') + k) % 26 + ord('A')
            result.append(chr(shifted))
        else:
            # Non‑alphabetic characters remain unchanged
            result.append(ch)

    return ''.join(result)
```