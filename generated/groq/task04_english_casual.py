```python
def is_palindrome(s: str) -> bool:
    """
    Return True if `s` reads the same forwards and backwards,
    ignoring case. Assumes `s` contains no spaces.
    """
    s_clean = s.lower()
    return s_clean == s_clean[::-1]
```