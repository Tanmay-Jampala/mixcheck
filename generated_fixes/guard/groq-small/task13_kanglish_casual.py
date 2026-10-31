```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lowercase sentence with no punctuation
    and single spaces between words.

    Parameters:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
    """
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```