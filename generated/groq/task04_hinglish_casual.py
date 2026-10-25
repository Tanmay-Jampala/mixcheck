```python
def is_palindrome(s: str) -> bool:
    """
    Return True if `s` reads the same forward and backward,
    ignoring case. Assumes the string contains no spaces.
    """
    s_clean = s.lower()
    return s_clean == s_clean[::-1]
```