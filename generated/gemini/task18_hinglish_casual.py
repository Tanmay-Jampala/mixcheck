```python
def sort_words(sentence):
    if not sentence:
        return []
    words = list(set(sentence.lower().split()))
    return sorted(words, key=lambda w: (len(w), w))
```