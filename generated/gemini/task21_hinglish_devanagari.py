```python
def caesar_shift(text, k):
    result = []
    k = k % 26
    for char in text:
        if 'a' <= char <= 'z':
            shifted = ord(char) + k
            if shifted > ord('z'):
                shifted -= 26
            result.append(chr(shifted))
        elif 'A' <= char <= 'Z':
            shifted = ord(char) + k
            if shifted > ord('Z'):
                shifted -= 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)
```