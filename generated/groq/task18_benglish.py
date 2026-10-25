```python
def sort_words(sentence: str) -> list:
    """
    Return a list of unique words from *sentence* in lowercase,
    sorted by length (shortest to longest) and alphabetically for equal lengths.
    """
    if not sentence:
        return []

    # split by spaces, normalize case, and keep unique words
    unique_words = {word.lower() for word in sentence.split()}

    # sort by length then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```