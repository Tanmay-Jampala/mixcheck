```python
def count_words(s: str) -> int:
    """Return the number of words in the string `s`.
    Words are separated by spaces; leading, trailing, and multiple
    consecutive spaces are ignored."""
    return len(s.split())
```