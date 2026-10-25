**Python function**

```python
def word_count(sentence: str) -> dict:
    """
    Count how many times each word appears in a sentence.

    Parameters
    ----------
    sentence : str
        A sentence that is already in lowercase, contains no punctuation
        and has words separated by a single space.

    Returns
    -------
    dict
        Keys are the words, values are the number of occurrences.
    """
    # Split on whitespace (single space is guaranteed, but split() works for any amount)
    words = sentence.split()

    # Count the words
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    return counts
```

**Example usage**

```python
>>> s = "the quick brown fox jumps over the lazy dog the quick"
>>> word_count(s)
{'the': 3, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1,
 'over': 1, 'lazy': 1, 'dog': 1}
```

If you prefer a one‑liner, you can use `collections.Counter`:

```python
from collections import Counter

def word_count(sentence: str) -> dict:
    return dict(Counter(sentence.split()))
```

Both versions give the same result.