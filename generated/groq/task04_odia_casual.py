```python
def is_palindrome(s: str) -> bool:
    """
    Return True if `s` is a palindrome when spaces are ignored
    and case is not considered; otherwise return False.
    """
    # Remove spaces and convert to a common case
    cleaned = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]
```