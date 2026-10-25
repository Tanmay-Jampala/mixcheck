```python
def caesar_shift(text, shift):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = ord('a') + (ord(char) - ord('a') + shift) % 26
            result.append(chr(shifted))
        elif 'A' <= char <= 'Z':
            shifted = ord('A') + (ord(char) - ord('A') + shift) % 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)
```