```python
def sort_words(sentence: str) -> list:
    """
    Return a list of unique words from the given sentence in lowercase,
    sorted by increasing length and alphabetically for equal lengths.

    Parameters
    ----------
    sentence : str
        A space‑separated sentence without punctuation.

    Returns
    -------
    list
        Sorted list of unique lowercase words.
    """
    if not sentence:
        return []

    # Split, normalize case, and keep unique words
    unique_words = {word.lower() for word in sentence.split()}

    # Sort by length then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```