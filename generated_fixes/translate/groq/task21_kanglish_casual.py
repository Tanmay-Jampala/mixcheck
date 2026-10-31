Here’s a compact, self‑contained implementation that follows the specification:

```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift every English alphabetic character in *text* forward by *k* positions.
    
    - Upper‑case letters stay upper‑case, lower‑case stay lower‑case.
    - The shift wraps around (e.g. 'z' → 'a', 'Z' → 'A').
    - All non‑letter characters (spaces, digits, punctuation, etc.) are left unchanged.
    
    Parameters
    ----------
    text : str
        The input string to be transformed.
    k : int
        Number of positions to shift.  Can be positive, negative, or zero.
    
    Returns
    -------
    str
        The Caesar‑shifted string.
    """
    # Normalise the shift to the range 0‑25 so large or negative values work correctly
    k = k % 26

    result_chars = []
    for ch in text:
        if 'a' <= ch <= 'z':                     # lower‑case
            # Compute offset from 'a', apply shift, wrap with modulo 26, convert back
            shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result_chars.append(shifted)
        elif 'A' <= ch <= 'Z':                   # upper‑case
            shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result_chars.append(shifted)
        else:                                    # non‑letter, keep as‑is
            result_chars.append(ch)

    return ''.join(result_chars)


# ----------------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    examples = [
        ("Hello, World!", 3),
        ("xyz XYZ", 2),
        ("Python3.8", -5),
        ("Caesar Cipher!", 0),
    ]

    for s, shift in examples:
        print(f"Original: {s!r}  shift={shift}")
        print(f"Encoded : {caesar_shift(s, shift)!r}")
        print("-" * 40)
```

### How it works
1. **Normalize the shift** – `k % 26` ensures that any integer (including negatives) maps to an equivalent shift within the 0‑25 range.
2. **Iterate over each character**:
   * If it’s a lower‑case letter, compute its alphabetical index (`ord(ch) - ord('a')`), add the shift, wrap with `% 26`, then convert back to a character.
   * The same logic applies to upper‑case letters, using `'A'` as the base.
   * All other characters are appended unchanged.
3. **Join** the list of processed characters into the final string.

Feel free to drop the function into any project, import it, or adapt the example block for quick testing.