```python
def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch != ' ')
    return cleaned == cleaned[::-1]
```