```python
def caesar_shift(text: str, k: int) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base + k) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base + k) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)
```