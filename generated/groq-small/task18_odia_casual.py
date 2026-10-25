```python
def sort_words(sentence):
    if not sentence or not sentence.strip():
        return []
    unique_words = {w.lower() for w in sentence.split()}
    return sorted(unique_words, key=lambda w: (len(w), w))
```