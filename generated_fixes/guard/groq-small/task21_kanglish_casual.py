```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift each English letter in `text` by `k` positions.
    Lowercase letters wrap from 'z' to 'a', uppercase from 'Z' to 'A'.
    Non-letter characters are left unchanged.
    """
    result = []
    k %= 26  # normalize shift
    for ch in text:
        if 'a' <= ch <= 'z':
            shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= ch <= 'Z':
            shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(ch)
    return ''.join(result)
```