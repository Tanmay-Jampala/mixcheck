```python
def sort_words(sentence: str) -> list[str]:
    """
    Return a list of unique words from `sentence` in lowercase,
    sorted by increasing length and alphabetically for equal lengths.
    If the sentence is empty, an empty list is returned.
    """
    if not sentence:
        return []

    # Split, normalize case, and deduplicate while preserving order of first appearance
    seen = set()
    words = []
    for w in sentence.split():
        lw = w.lower()
        if lw not in seen:
            seen.add(lw)
            words.append(lw)

    # Sort by length then alphabetically
    words.sort(key=lambda w: (len(w), w))
    return words
```