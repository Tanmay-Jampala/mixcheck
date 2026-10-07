```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string `s` (without spaces) is a palindrome,
    ignoring case differences; otherwise return False.

    Example:
        >>> is_palindrome("Racecar")
        True
    """
    # Normalize case
    s_lower = s.lower()
    # Compare with its reverse
    return s_lower == s_lower[::-1]
```