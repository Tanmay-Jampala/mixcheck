```python
def sort_words(sentence):
    if not sentence.strip():
        return []
    words = list(set(sentence.lower().split()))
    return sorted(words, key=lambda w: (len(w), w))
```