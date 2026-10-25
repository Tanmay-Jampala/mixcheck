```python
def sort_words(naam):
    if not naam:
        return []
    unique_words = {word.lower() for word in naam.split()}
    return sorted(unique_words, key=lambda w: (len(w), w))
```