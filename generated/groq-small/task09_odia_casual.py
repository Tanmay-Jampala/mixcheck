```python
def count_words(s: str) -> int:
    """
    Count the number of words in a string.
    Words are separated by spaces; leading, trailing, or multiple spaces are ignored.
    """
    return len(s.strip().split())
```