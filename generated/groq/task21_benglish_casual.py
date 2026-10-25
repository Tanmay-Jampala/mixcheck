```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift each English letter in `text` by `k` positions.
    - Wraps around after 'z' → 'a' and 'Z' → 'A'.
    - Preserves the case of each letter.
    - Non‑alphabetic characters (spaces, digits, punctuation, etc.) are left unchanged.
    """
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # Compute shifted position for lowercase
            offset = (ord(ch) - ord('a') + k) % 26
            result.append(chr(ord('a') + offset))
        elif 'A' <= ch <= 'Z':
            # Compute shifted position for uppercase
            offset = (ord(ch) - ord('A') + k) % 26
            result.append(chr(ord('A') + offset))
        else:
            # Non‑alphabetic characters stay the same
            result.append(ch)

    return ''.join(result)
```