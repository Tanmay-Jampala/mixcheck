```python
def sort_words(sentence):
    if not sentence or not sentence.strip():
        return []

    words = set(sentence.lower().split())

    return sorted(words, key=lambda w: (len(w), w))
```