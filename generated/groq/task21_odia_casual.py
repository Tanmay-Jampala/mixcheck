```python
def caesar_shift(text: str, k: int) -> str:
    """Shift each English letter in *text* forward by *k* positions.
    Wraps around after 'z'/'Z', preserves case, and leaves non‑letters unchanged.
    """
    k %= 26  # effective shift
    shifted = []

    for ch in text:
        if 'a' <= ch <= 'z':
            shifted.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            shifted.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            shifted.append(ch)

    return ''.join(shifted)


# Example usage:
if __name__ == "__main__":
    s = "Hello, World! 123"
    k = 5
    print(caesar_shift(s, k))   # "Mjqqt, Btwqi! 123"
```