```python
def capitalize_words(sentence: str) -> str:
    """Capitalize the first letter of each word in a lowercase sentence."""
    return ' '.join(word.capitalize() for word in sentence.split(' '))
```