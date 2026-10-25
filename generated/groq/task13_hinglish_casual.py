```python
def word_count(sentence: str) -> dict:
    """Return a dictionary with the frequency of each word in a lowercase,
    punctuation‑free, single‑spaced sentence."""
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq
```