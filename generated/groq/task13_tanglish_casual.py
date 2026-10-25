```python
def word_count(sentence: str) -> dict[str, int]:
    """
    Count the occurrences of each word in a lowercase sentence.

    Assumptions:
    - The sentence contains only lowercase letters, spaces, and no punctuation.
    - Words are separated by a single space.

    Parameters
    ----------
    sentence: str
        The input sentence.

    Returns
    -------
    dict[str, int]
        Mapping of each word to its frequency.
    """
    counts: dict[str, int] = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```