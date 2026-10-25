```python
def caesar_shift(text, k):
    """Shift each English letter in `text` by `k` positions."""
    k %= 26  # normalize shift
    result = []

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