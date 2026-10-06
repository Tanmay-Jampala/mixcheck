```python
def is_palindrome(s: str) -> bool:
    normalized = s.lower()
    return normalized == normalized[::-1]
```