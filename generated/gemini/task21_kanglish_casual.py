```python
def caesar_shift(text, k):
    result = []
    for char in text:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + k) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + k) % 26 + ord("A"))
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)
```