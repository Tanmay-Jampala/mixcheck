```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase, space‑separated sentence.

    Parameters
    ----------
    sentence : str
        A sentence containing only lowercase letters and single spaces
        (no punctuation).

    Returns
    -------
    dict
        Mapping from each word to its frequency in the sentence.
    """
    # If the sentence is empty, return an empty dictionary
    if not sentence:
        return {}

    # Split on spaces (guaranteed single spaces) and count
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```