Here’s a compact, self‑contained implementation of `count_vowels`.  
It works for any string, counts both lowercase and uppercase vowels, and returns the total number of vowels found.

```python
def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the given string.
    Vowels are counted case‑insensitively.

    Parameters
    ----------
    s : str
        The string to examine.

    Returns
    -------
    int
        The total count of vowels in `s`.
    """
    # Define the set of vowels for quick membership tests
    vowels = set("aeiouAEIOU")

    # Sum 1 for each character that is a vowel
    return sum(1 for ch in s if ch in vowels)


# Example usage
if __name__ == "__main__":
    test_str = "Hello, World! 123"
    print(f"Vowels in '{test_str}': {count_vowels(test_str)}")  # Output: 3
```

### How it works
1. **`vowels` set** – A set of all vowel characters (both lowercase and uppercase) gives O(1) lookup time.
2. **Generator expression** – Iterates over each character in the input string, adding `1` to the sum whenever the character is in the `vowels` set.
3. **Return** – The final integer count is returned.

Feel free to drop this function into any module or script where you need vowel counting!