Here’s a clean, reusable **`is_palindrome`** function that follows exactly what you asked for:

* **Ignores spaces** – they are stripped out before the check.  
* **Case‑insensitive** – treats “A” and “a” as the same character.  
* Returns **`True`** if the cleaned string reads the same forward and backward, otherwise **`False`**.

```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome when spaces are ignored
    and case is not considered.

    Parameters
    ----------
    s : str
        The input string to test.

    Returns
    -------
    bool
        True  -> palindrome (ignoring spaces & case)
        False -> not a palindrome
    """
    # 1. Remove all spaces
    no_spaces = s.replace(" ", "")
    # 2. Convert to a single case (lowercase)
    normalized = no_spaces.lower()
    # 3. Compare with its reverse
    return normalized == normalized[::-1]


# -------------------------------------------------
# Example usage
if __name__ == "__main__":
    test_cases = [
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "Hello World",
        "Madam",
        "No lemon no melon",
        "  ",                     # only spaces -> considered palindrome
        "",                       # empty string -> palindrome
    ]

    for txt in test_cases:
        print(f"{txt!r:30} -> {is_palindrome(txt)}")
```

### How it works
1. **`s.replace(" ", "")`** removes every space character.  
   (If you also want to ignore other whitespace like tabs or new‑lines, use `''.join(s.split())` instead.)

2. **`.lower()`** normalises the string so that `'A'` and `'a'` are treated the same.

3. **`normalized[::-1]`** creates the reversed version of the cleaned string.  
   If the cleaned string equals its reverse, it’s a palindrome.

### Quick test

```python
>>> is_palindrome("A man a plan a canal Panama")
True
>>> is_palindrome("Hello World")
False
>>> is_palindrome("Madam")
True
```

Feel free to drop this function into any of your projects! 🚀