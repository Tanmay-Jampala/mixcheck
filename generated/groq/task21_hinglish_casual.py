```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift every English alphabetic character in `text` by `k` positions.
    - Upper‑case letters stay upper‑case, lower‑case stay lower‑case.
    - Non‑alphabetic characters (space, digits, punctuation, etc.) are left unchanged.
    - Supports positive and negative shifts; wraps around the alphabet (a↔z).

    Parameters
    ----------
    text : str
        Input string to be shifted.
    k : int
        Number of positions to shift (positive = forward, negative = backward).

    Returns
    -------
    str
        The shifted string.
    """
    result = []

    # Normalize shift to range [0, 25] to avoid unnecessary large loops
    k = k % 26

    for ch in text:
        if 'a' <= ch <= 'z':
            # Compute shifted position for lowercase
            shifted = (ord(ch) - ord('a') + k) % 26 + ord('a')
            result.append(chr(shifted))
        elif 'A' <= ch <= 'Z':
            # Compute shifted position for uppercase
            shifted = (ord(ch) - ord('A') + k) % 26 + ord('A')
            result.append(chr(shifted))
        else:
            # Non‑alphabetic characters are unchanged
            result.append(ch)

    return ''.join(result)


# Example usage:
if __name__ == "__main__":
    print(caesar_shift("Hello, World! 123", 3))   # Khoor, Zruog! 123
    print(caesar_shift("Khoor, Zruog! 123", -3))  # Hello, World! 123
```
This function meets all the requirements: it shifts only English letters, preserves case, wraps around after `z`/`Z`, and leaves all other characters untouched.