```python
def count_words(s: str) -> int:
    """
    Return the number of words in the given string.

    Words are sequences of characters separated by whitespace.
    Leading, trailing, or multiple consecutive spaces are ignored.
    """
    # str.split() without arguments splits on any whitespace and discards empties
    return len(s.split())
```