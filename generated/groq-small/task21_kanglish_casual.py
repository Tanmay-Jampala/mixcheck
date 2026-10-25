**Python – Caesar‑Shift (English letters only)**  

```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift every English letter in *text* by *k* positions.
    
    Parameters
    ----------
    text : str
        The string to be shifted.
    k : int
        Number of positions to shift.  Positive values shift forward,
        negative values shift backward.  The shift wraps around the
        alphabet (z → a, Z → A).

    Returns
    -------
    str
        The shifted string.  Non‑letters (spaces, digits, punctuation,
        etc.) are left untouched.
    """
    # Normalise k to the range 0‑25 so that large values or negatives
    # are handled correctly.
    k = k % 26

    result = []

    for ch in text:
        # Upper‑case letters
        if 'A' <= ch <= 'Z':
            # 0‑based index of the letter in the alphabet
            idx = ord(ch) - ord('A')
            # Shift and wrap
            new_idx = (idx + k) % 26
            result.append(chr(ord('A') + new_idx))
        # Lower‑case letters
        elif 'a' <= ch <= 'z':
            idx = ord(ch) - ord('a')
            new_idx = (idx + k) % 26
            result.append(chr(ord('a') + new_idx))
        # Non‑letters stay the same
        else:
            result.append(ch)

    return ''.join(result)
```

### Quick examples

```python
print(caesar_shift("Hello, World!", 3))
# Output: Khoor, Zruog!

print(caesar_shift("abcXYZ", 2))
# Output: cdeZAB

print(caesar_shift("Python 3.8", -5))
# Output: Ktqfkd 3.8
```

### How it works

1. **Normalize `k`** – `k % 26` guarantees the shift stays within the alphabet.
2. **Iterate over each character** –  
   * If it’s an uppercase letter (`'A'`–`'Z'`), compute its 0‑based index, shift it, wrap with modulo 26, and convert back to a character.  
   * If it’s a lowercase letter (`'a'`–`'z'`), do the same with the lowercase alphabet.  
   * Any other character is appended unchanged.
3. **Return** the joined list of characters.

Feel free to drop this function into your project or tweak it (e.g., to support other alphabets). Happy coding!