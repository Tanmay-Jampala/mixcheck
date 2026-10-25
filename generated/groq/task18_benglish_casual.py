```python
def sort_words(sentence: str) -> list:
    """
    Returns a list of unique words from the given sentence.
    - Words are treated case‑insensitively and returned in lowercase.
    - Sorted by length (shortest first); words of equal length are sorted alphabetically.
    - If the sentence is empty, returns an empty list.
    """
    if not sentence:
        return []

    # Split, normalize case, and keep unique words
    unique_words = {word.lower() for word in sentence.split()}

    # Sort by length, then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```