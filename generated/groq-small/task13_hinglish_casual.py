```python
def word_count(sentence: str) -> dict:
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```