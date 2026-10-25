```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase sentence
    that contains no punctuation and uses a single space between words.
    """
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```