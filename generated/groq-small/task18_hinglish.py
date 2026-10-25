```python
def sort_words(sentence: str) -> list[str]:
    if not sentence or not sentence.strip():
        return []

    # Split on spaces, convert to lowercase, keep unique words
    unique_words = {word.lower() for word in sentence.split()}

    # Sort by length first, then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```