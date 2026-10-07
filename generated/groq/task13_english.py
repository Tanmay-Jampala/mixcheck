```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase, space‑separated sentence.

    Parameters
    ----------
    sentence : str
        A string containing only lowercase words separated by single spaces.

    Returns
    -------
    dict
        A dictionary mapping each word to its frequency.
    """
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```