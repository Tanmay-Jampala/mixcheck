```python
def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            # Uppercase letters (A-Z)
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(ord('A') + shifted)
        elif char.islower():
            # Lowercase letters (a-z)
            shifted = (ord(char) - ord('a') + shift) % 26
            result += chr(ord('a') + shifted)
        else:
            # Spaces, digits, punctuation remain unchanged
            result += char
    return result
```