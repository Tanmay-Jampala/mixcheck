```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string is a palindrome when spaces are ignored
    and case is not considered; otherwise return False.
    """
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]
```