```python
def sort_words(sentence: str):
    if not sentence:
        return []
    # Split by single space, convert to lowercase for uniqueness
    unique_words = {word.lower() for word in sentence.split()}
    # Sort by length, then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```