```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase sentence without punctuation.

    Parameters:
        sentence (str): A string containing words separated by single spaces.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
    """
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```