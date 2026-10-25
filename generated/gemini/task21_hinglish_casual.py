```python
def caesar_shift(text, k):
    result = []
    k = k % 26  # 26 se zyada shift ko normalize karne ke liye

    for char in text:
        if 'a' <= char <= 'z':
            # Small letters ke liye
            shifted = ord(char) + k
            if shifted > ord('z'):
                shifted -= 26
            result.append(chr(shifted))
        elif 'A' <= char <= 'Z':
            # Capital letters ke liye
            shifted = ord(char) + k
            if shifted > ord('Z'):
                shifted -= 26
            result.append(chr(shifted))
        else:
            # Jo letters nahi hain (space, punctuation, digits)
            result.append(char)

    return "".join(result)
```