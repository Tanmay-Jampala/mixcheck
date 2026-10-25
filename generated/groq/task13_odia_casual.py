```python
def word_count(sentence: str) -> dict:
    """
    Count occurrences of each word in a lowercase, space‑separated sentence.
    Assumes the input contains no punctuation and words are separated by a single space.
    """
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```