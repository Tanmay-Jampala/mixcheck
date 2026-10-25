```python
def capitalize_words(sentence: str) -> str:
    """
    Convert a lowercase sentence with words separated by single spaces
    so that the first letter of each word is capitalized.
    """
    return ' '.join(word.capitalize() for word in sentence.split(' '))
```