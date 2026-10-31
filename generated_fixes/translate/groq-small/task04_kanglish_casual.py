Here’s a compact, self‑contained implementation that meets the requirements:

```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome, ignoring case.
    
    Parameters
    ----------
    s : str
        The string to test.  It may contain any characters; spaces are
        ignored automatically because the comparison is case‑insensitive
        and we simply reverse the string.
    
    Returns
    -------
    bool
        True if `s` reads the same forward and backward (case‑insensitive),
        False otherwise.
    """
    # Normalize to a single case (lowercase) and compare with its reverse.
    normalized = s.lower()
    return normalized == normalized[::-1]


# Example usage
if __name__ == "__main__":
    tests = ["Racecar", "Hello", "Madam", "Step on no pets", "Was it a car or a cat I saw"]
    for t in tests:
        # Remove spaces for the test, as the spec says "without spaces"
        t_no_spaces = t.replace(" ", "")
        print(f"{t!r} → {is_palindrome(t_no_spaces)}")
```

**Explanation**

1. `s.lower()` converts the entire string to lowercase, so the comparison is case‑insensitive.
2. `normalized[::-1]` creates a reversed copy of the string.
3. The equality check returns `True` only if the string is identical to its reverse.

The example usage demonstrates how the function behaves with various inputs, stripping spaces before testing to satisfy the “without spaces” requirement.