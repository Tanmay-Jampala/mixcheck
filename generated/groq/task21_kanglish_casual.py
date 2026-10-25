Here’s a compact, well‑documented implementation of a **Caesar‑shift** function that follows exactly the rules you described:

```python
def caesar_shift(text: str, k: int) -> str:
    """
    Shift every English alphabetic character in *text* forward by *k* positions.
    
    * Upper‑case letters stay upper‑case, lower‑case stay lower‑case.
    * The alphabet wraps around (… x → y → z → a → b …).
    * All non‑alphabetic characters (space, digits, punctuation, etc.) are left unchanged.
    
    Parameters
    ----------
    text : str
        The input string to be encoded.
    k : int
        Number of positions to shift.  Can be any integer (positive, zero or negative).

    Returns
    -------
    str
        The shifted string.
    """
    result = []

    # Normalise the shift to the range 0‑25 so huge values work as well
    k = k % 26

    for ch in text:
        if 'a' <= ch <= 'z':                     # lower‑case
            # ord('a') = 97
            shifted = (ord(ch) - ord('a') + k) % 26 + ord('a')
            result.append(chr(shifted))
        elif 'A' <= ch <= 'Z':                   # upper‑case
            # ord('A') = 65
            shifted = (ord(ch) - ord('A') + k) % 26 + ord('A')
            result.append(chr(shifted))
        else:                                    # any other character
            result.append(ch)

    return ''.join(result)


# ------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    s = "Hello, World! 123"
    k = 3
    print("Original :", s)
    print("Shifted  :", caesar_shift(s, k))
    # Output → "Khoor, Zruog! 123"
```

### How it works
1. **Normalize the shift** – `k % 26` makes sure that a shift of, say, 30 is treated the same as a shift of 4.
2. **Iterate over each character**  
   * If it’s a lower‑case letter, compute its 0‑based index (`ord(ch) - ord('a')`), add the shift, wrap with `% 26`, then convert back to a character.  
   * The same logic is applied for upper‑case letters, using `'A'` as the base.  
   * Anything else (`space`, digits, punctuation, etc.) is appended unchanged.
3. **Join** the list of characters back into a single string.

Feel free to drop the function into any project; it works with Python 3.x out of the box.