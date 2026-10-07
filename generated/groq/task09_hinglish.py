```python
def count_words(text: str) -> int:
    """Return the number of words in *text*.
    
    Words are sequences of characters separated by whitespace.
    Leading, trailing, or multiple intermediate spaces are ignored.
    """
    return len(text.split())
```