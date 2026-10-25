```python
def sort_words(sentence: str) -> list:
    """
    Return a list of unique words from `sentence` in lowercase,
    sorted by increasing length and alphabetically for equal lengths.
    An empty sentence yields an empty list.
    """
    if not sentence:
        return []

    # Split, normalize case, and keep unique words
    unique_words = {word.lower() for word in sentence.split()}

    # Sort by length then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```