```python
def count_words(s: str) -> int:
    """
    Count the number of words in a string.
    Words are separated by spaces; leading, trailing, or multiple
    consecutive spaces are ignored.
    """
    return len(s.split())
```