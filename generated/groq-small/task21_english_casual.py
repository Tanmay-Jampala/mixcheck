```python
def caesar_shift(text, k):
    """Shift every English letter in `text` by `k` positions forward.
    Wrap around from 'z' to 'a' (or 'Z' to 'A'). Preserve case.
    Non‑letters are left unchanged."""
    k %= 26  # normalize shift
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # shift lowercase
            shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= ch <= 'Z':
            # shift uppercase
            shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        else:
            # keep non‑letters unchanged
            result.append(ch)

    return ''.join(result)
```