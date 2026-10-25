```python
def caesar_shift(text: str, k: int) -> str:
    """Shift each English letter in *text* forward by *k* positions.
    
    Uppercase letters stay uppercase, lowercase stay lowercase.
    Non‑alphabetic characters are left unchanged.
    """
    result = []
    k %= 26  # effective shift

    for ch in text:
        if 'a' <= ch <= 'z':
            # Compute shifted position within lowercase alphabet
            shifted = (ord(ch) - ord('a') + k) % 26 + ord('a')
            result.append(chr(shifted))
        elif 'A' <= ch <= 'Z':
            # Compute shifted position within uppercase alphabet
            shifted = (ord(ch) - ord('A') + k) % 26 + ord('A')
            result.append(chr(shifted))
        else:
            # Non‑letter characters are unchanged
            result.append(ch)

    return ''.join(result)
```