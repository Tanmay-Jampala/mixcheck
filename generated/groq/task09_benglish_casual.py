```python
def count_words(s: str) -> int:
    """
    Return the number of words in the given string.
    Words are separated by spaces; leading, trailing, or multiple
    consecutive spaces are ignored.
    """
    # split() without arguments splits on any whitespace and discards empties
    return len(s.split())
```