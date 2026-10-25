```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift every English letter in `text` forward by `k` positions.
    Wraps around after 'z'/'Z', keeps case, leaves non‑letters unchanged.
    """
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # shift lowercase
            offset = (ord(ch) - ord('a') + k) % 26
            result.append(chr(ord('a') + offset))
        elif 'A' <= ch <= 'Z':
            # shift uppercase
            offset = (ord(ch) - ord('A') + k) % 26
            result.append(chr(ord('A') + offset))
        else:
            # non‑letter stays the same
            result.append(ch)

    return ''.join(result)
```