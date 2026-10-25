```python
def word_count(sentence: str) -> dict:
    words = sentence.split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
```