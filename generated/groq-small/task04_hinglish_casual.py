```python
def is_palindrome(s: str) -> bool:
    """
    Returns True if the given string is a palindrome, ignoring case.
    Assumes the string contains no spaces.
    """
    s = s.lower()
    return s == s[::-1]
```