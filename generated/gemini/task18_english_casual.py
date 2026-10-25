```python
def sort_words(sentence: str) -> list[str]:
    if not sentence:
        return []
    words = set(sentence.lower().split())
    return sorted(words, key=lambda w: (len(w), w))
```