```python
def word_count(sentence: str) -> dict:
    """Return a dictionary with the frequency of each word in a lowercase,
    space‑separated sentence (no punctuation)."""
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```