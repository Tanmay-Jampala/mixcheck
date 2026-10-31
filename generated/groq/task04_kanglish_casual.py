Here’s a compact, case‑insensitive palindrome checker that ignores spaces (and any other whitespace characters).  

```python
def is_palindrome(s: str) -> bool:
    """
    Return True if `s` reads the same forward and backward,
    ignoring spaces and case differences.

    Parameters
    ----------
    s : str
        The string to test.

    Returns
    -------
    bool
        True  – `s` is a palindrome (ignoring spaces & case)
        False – otherwise
    """
    # Remove all whitespace and convert to a single case
    cleaned = ''.join(ch for ch in s if not ch.isspace()).lower()
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]


# ------------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    tests = [
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "Hello World",
        "RaceCar",
        "  ",
        "No lemon, no melon"
    ]

    for txt in tests:
        print(f"{txt!r:30} -> {is_palindrome(txt)}")
```

**Explanation**

1. **`''.join(ch for ch in s if not ch.isspace())`**  
   – Builds a new string that contains every character from `s` except whitespace (`' '`, `'\t'`, `'\n'`, …).

2. **`.lower()`**  
   – Normalises the case so that `'A'` and `'a'` are treated the same.

3. **`cleaned == cleaned[::-1]`**  
   – Checks whether the processed string is identical to its reverse (`[::-1]` slices the string backwards).

The function returns `True` only when the original string is a palindrome after ignoring spaces and case differences. Feel free to adapt the whitespace filter (e.g., also strip punctuation) if you need a stricter definition.