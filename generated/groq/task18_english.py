```python
def sort_words(sentence: str) -> list[str]:
    """
    Return a list of unique words from *sentence* in lowercase,
    sorted by length (shortest to longest). Words of equal length
    are sorted alphabetically.

    Parameters
    ----------
    sentence: str
        A space‑separated string with no punctuation.

    Returns
    -------
    list[str]
        Sorted list of unique words, or an empty list if *sentence* is empty.
    """
    if not sentence:
        return []

    # Split, normalize case, and deduplicate while preserving order of first appearance
    words = {word.lower() for word in sentence.split()}

    # Sort by length then alphabetically
    return sorted(words, key=lambda w: (len(w), w))
```