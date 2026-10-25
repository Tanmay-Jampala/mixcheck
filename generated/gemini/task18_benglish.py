```python
def sort_words(sentence):
    if not sentence.strip():
        return []
    
    words = sentence.lower().split()
    unique_words = sorted(list(set(words)))
    unique_words.sort(key=len)
    
    return unique_words
```