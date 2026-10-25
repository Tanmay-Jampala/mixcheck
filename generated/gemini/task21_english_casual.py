```python
def caesar_shift(text, k):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(char)
    return "".join(result)
```