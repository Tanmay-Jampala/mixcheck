```python
def word_count(sentence: str) -> dict:
    """Return a dictionary of word counts for a lowercase sentence with single spaces."""
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```