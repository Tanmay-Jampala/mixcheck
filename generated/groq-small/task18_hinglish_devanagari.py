```python
def sort_words(sentence):
    if not sentence:
        return []
    unique_words = {word.lower() for word in sentence.split()}
    return sorted(unique_words, key=lambda w: (len(w), w))
```