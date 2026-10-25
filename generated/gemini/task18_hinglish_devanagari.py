```python
def sort_words(sentence):
    if not sentence.strip():
        return []
    words = list(set(word.lower() for word in sentence.split()))
    return sorted(words, key=lambda w: (len(w), w))
```