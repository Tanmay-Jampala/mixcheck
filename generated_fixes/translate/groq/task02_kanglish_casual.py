Here’s a simple, self‑contained implementation. It works for both lower‑ and upper‑case vowels and ignores any other characters.

```python
def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the given string.

    The check is case‑insensitive, so both 'A' and 'a' (and the other
    vowels) are counted.

    Parameters
    ----------
    s : str
        The input string to examine.

    Returns
    -------
    int
        The total count of vowel characters in ``s``.
    """
    # A set gives O(1) membership tests and makes the code easy to read.
    vowels = set('aeiouAEIOU')
    return sum(1 for ch in s if ch in vowels)


# ----------------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    examples = [
        "Hello, World!",
        "Python",
        "AEIOUaeiou",
        "",
        "12345!@#",
        "The quick brown fox jumps over the lazy dog"
    ]

    for txt in examples:
        print(f"{txt!r:40} → {count_vowels(txt)} vowel(s)")
```

**Explanation**

1. **`vowels` set** – contains all six vowel letters in both lower‑ and upper‑case.  
2. **Generator expression** – `1 for ch in s if ch in vowels` yields a `1` for each vowel found.  
3. **`sum`** – adds up those `1`s, giving the total count.

Running the script will print the vowel count for each example string. Feel free to drop the function into any larger program or module you’re building.