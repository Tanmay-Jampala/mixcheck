```python
def sort_words(sentence: str) -> list[str]:
    """
    Return the unique words in the sentence in lowercase, sorted by length
    (shortest first). Words of the same length are sorted alphabetically.
    Empty sentence returns an empty list.
    """
    if not sentence:
        return []

    # Split on whitespace, normalize to lowercase, keep unique words
    unique_words = {w.lower() for w in sentence.split()}

    # Sort by length first, then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```