Here’s a compact, self‑contained implementation that follows the specification:

```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase sentence.

    Parameters
    ----------
    sentence : str
        A sentence that contains only lowercase letters, single spaces
        between words, and no punctuation.

    Returns
    -------
    dict
        A dictionary where each key is a word from the sentence and the
        corresponding value is the number of times that word appears.
    """
    # Split the sentence into words (single spaces guarantee a clean split)
    words = sentence.split()

    # Count the words
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    return counts
```

### Example

```python
>>> word_count("the quick brown fox jumps over the lazy dog the")
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

The function uses a simple dictionary to accumulate counts, which is efficient and works for any length of input sentence that satisfies the stated constraints.