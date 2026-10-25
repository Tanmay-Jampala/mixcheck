```python
def sort_words(sentence: str) -> list[str]:
    """
    Return a list of the unique words in *sentence* (case‑insensitive),
    all in lowercase, sorted by length (shortest first) and then
    alphabetically for words of equal length.

    The input sentence contains only single spaces and no punctuation.
    An empty sentence yields an empty list.
    """
    if not sentence:
        return []

    # Split, normalise case and deduplicate
    unique = {word.lower() for word in sentence.split()}

    # Sort by length then alphabetically
    return sorted(unique, key=lambda w: (len(w), w))
```