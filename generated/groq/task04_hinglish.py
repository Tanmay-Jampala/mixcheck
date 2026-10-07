```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string `s` is a palindrome,
    ignoring case. Assumes `s` contains no spaces.
    """
    s_lower = s.lower()
    return s_lower == s_lower[::-1]
```