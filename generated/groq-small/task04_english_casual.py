```python
def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards, ignoring case."""
    s = s.lower()
    return s == s[::-1]
```