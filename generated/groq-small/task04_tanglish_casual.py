```python
def is_palindrome(s: str) -> bool:
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]
```