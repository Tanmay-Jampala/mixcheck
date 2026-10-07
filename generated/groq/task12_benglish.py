```python
def capitalize_words(sentence: str) -> str:
    """
    Convert a lowercase sentence to title case, capitalizing the first
    letter of each word. Assumes words are separated by a single space.

    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    # Split the sentence into words, capitalize each, then join back.
    words = sentence.split(' ')
    capitalized = [word[:1].upper() + word[1:] for word in words]
    return ' '.join(capitalized)
```