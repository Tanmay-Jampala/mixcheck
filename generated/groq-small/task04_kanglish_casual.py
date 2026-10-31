**Python – `is_palindrome` ಫಂಕ್ಷನ್ (spaces ಅಗಣಿಸಿ, case‑insensitive)**  

```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome.
    
    Rules:
    * Spaces are ignored.
    * Upper‑case / lower‑case letters are treated as the same.
    * All other characters (punctuation, digits, etc.) are considered part of the string.
    
    Examples
    --------
    >>> is_palindrome("Madam In Eden, I'm Adam")
    True
    >>> is_palindrome("Hello World")
    False
    """
    # 1. Remove all spaces
    cleaned = s.replace(" ", "")
    # 2. Make it case‑insensitive
    cleaned = cleaned.lower()
    # 3. Compare with its reverse
    return cleaned == cleaned[::-1]


# Quick sanity‑check
if __name__ == "__main__":
    tests = [
        ("Madam In Eden, I'm Adam", True),
        ("Hello World", False),
        ("A man a plan a canal Panama", True),
        ("No lemon no melon", True),
        ("Was it a car or a cat I saw", True),
        ("Not a palindrome", False),
    ]

    for txt, expected in tests:
        result = is_palindrome(txt)
        print(f"{txt!r:40} -> {result} (expected {expected})")
```

### How it works

1. **Remove spaces** – `s.replace(" ", "")` gives a new string without any space characters.  
2. **Normalize case** – `lower()` turns everything into lower‑case, so `"A"` and `"a"` are treated the same.  
3. **Palindrome check** – `cleaned == cleaned[::-1]` compares the string with its reverse.  
   * `[::-1]` is a slice that returns the string reversed.  
   * If they match, the string is a palindrome; otherwise it isn’t.

Feel free to drop this function into your project or tweak it (e.g., to ignore punctuation as well).