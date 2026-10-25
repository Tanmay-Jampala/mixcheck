```python
def sort_words(sentence: str) -> list[str]:
    """
    Return unique words from the sentence in lowercase, sorted by length (ascending)
    and alphabetically for words of the same length.
    If the sentence is empty or contains only whitespace, return an empty list.
    """
    # Strip leading/trailing whitespace and check for emptiness
    sentence = sentence.strip()
    if not sentence:
        return []

    # Split on single spaces, convert to lowercase, and keep unique words
    words = {word.lower() for word in sentence.split(' ')}

    # Sort by length first, then alphabetically
    return sorted(words, key=lambda w: (len(w), w))
```