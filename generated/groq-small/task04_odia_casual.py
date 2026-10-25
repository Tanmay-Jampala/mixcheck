```python
def is_palindrome(s: str) -> bool:
    # No spaces allowed
    if ' ' in s:
        return False
    # Case‑sensitive palindrome check
    return s == s[::-1]
```