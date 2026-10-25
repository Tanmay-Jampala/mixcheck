```python
def count_words(s: str) -> int:
    """Return the number of words in *s*.
    
    Words are separated by whitespace. Leading, trailing, or multiple
    consecutive spaces are ignored.
    """
    return len(s.split())
```