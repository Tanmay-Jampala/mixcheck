```python
def sort_words(sentence: str) -> list:
    if not sentence.strip():
        return []
    words = list(set(sentence.lower().split()))
    return sorted(words, key=lambda w: (len(w), w))
```