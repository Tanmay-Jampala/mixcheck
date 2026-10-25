```python
def caesar_shift(text, shift):
    """
    Shift each alphabetic character in `text` by `shift` positions.
    Uppercase letters stay uppercase, lowercase stay lowercase.
    Non‑alphabetic characters are unchanged.
    """
    shift %= 26  # normalize shift to range 0-25
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            # shift lowercase letter
            offset = ord('a')
            new_char = chr((ord(ch) - offset + shift) % 26 + offset)
            result.append(new_char)
        elif 'A' <= ch <= 'Z':
            # shift uppercase letter
            offset = ord('A')
            new_char = chr((ord(ch) - offset + shift) % 26 + offset)
            result.append(new_char)
        else:
            # non‑alphabetic characters remain unchanged
            result.append(ch)

    return ''.join(result)
```