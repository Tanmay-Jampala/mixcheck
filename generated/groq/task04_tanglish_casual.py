```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome.
    - Ignores spaces.
    - Case‑insensitive.
    """
    # Remove spaces and convert to lower case
    cleaned = ''.join(ch.lower() for ch in s if ch != ' ')
    # Check palindrome
    return cleaned == cleaned[::-1]
```