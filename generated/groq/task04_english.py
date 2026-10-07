```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string reads the same forwards and backwards,
    ignoring case. The input string is assumed to contain no spaces.
    """
    s_clean = s.lower()
    return s_clean == s_clean[::-1]
```