```python
def capitalize_words(sentence: str) -> str:
    """Convert a lowercase sentence to title case (first letter of each word uppercase)."""
    return ' '.join(word.capitalize() for word in sentence.split(' '))
```