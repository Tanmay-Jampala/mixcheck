```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string `s` (without spaces) is a palindrome,
    ignoring case differences. Otherwise return False.
    """
    s_clean = s.lower()
    return s_clean == s_clean[::-1]
```