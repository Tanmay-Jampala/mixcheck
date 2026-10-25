```python
def sort_words(sentence):
    if not sentence:
        return []
    words = set(sentence.lower().split())
    return sorted(list(words), key=lambda w: (len(w), w))
```