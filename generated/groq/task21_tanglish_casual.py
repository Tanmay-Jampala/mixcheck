```python
def caesar_shift(text: str, k: int) -> str:
    """Shift each English letter in *text* by *k* positions.
    Upper‑case letters stay upper‑case, lower‑case stay lower‑case.
    Non‑letter characters are left unchanged.
    """
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # ord('a') = 97
            shifted = (ord(ch) - ord('a') + k) % 26 + ord('a')
            result.append(chr(shifted))
        elif 'A' <= ch <= 'Z':
            # ord('A') = 65
            shifted = (ord(ch) - ord('A') + k) % 26 + ord('A')
            result.append(chr(shifted))
        else:
            result.append(ch)

    return ''.join(result)


# Example usage
if __name__ == "__main__":
    s = "Hello, World! 123"
    k = 3
    print(caesar_shift(s, k))   # Khoor, Zruog! 123
```