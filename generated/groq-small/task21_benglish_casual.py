```python
def caesar_shift(text, k):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            offset = (ord(ch) - ord('a') + k) % 26
            result.append(chr(ord('a') + offset))
        elif 'A' <= ch <= 'Z':
            offset = (ord(ch) - ord('A') + k) % 26
            result.append(chr(ord('A') + offset))
        else:
            result.append(ch)
    return ''.join(result)
```