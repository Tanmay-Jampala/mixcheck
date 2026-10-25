```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase sentence.
    Assumes the sentence contains only single spaces and no punctuation.
    """
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```