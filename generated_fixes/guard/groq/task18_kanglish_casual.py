```python
def sort_words(sentence: str):
    """
    Return a list of unique words from the given sentence.
    - Words are treated case‑insensitively and returned in lowercase.
    - Sorted first by length (shortest first), then alphabetically for equal lengths.
    - If the sentence is empty or contains only whitespace, an empty list is returned.
    """
    # Trim and handle empty input
    if not sentence or not sentence.strip():
        return []

    # Split on whitespace, normalize case, and keep unique words
    unique_words = {word.lower() for word in sentence.split()}

    # Sort by length then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```