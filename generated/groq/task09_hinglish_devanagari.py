```python
def count_words(s: str) -> int:
    # Split on whitespace and filter out any empty strings
    return len([word for word in s.split() if word])
```