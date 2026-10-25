```python
def sort_words(sentence: str) -> list[str]:
    """
    Return a list of unique words from *sentence* in lowercase,
    sorted by increasing length and then alphabetically for equal lengths.

    Assumptions:
    - *sentence* contains only words separated by a single space.
    - No punctuation is present.
    - The function is case‑insensitive; the output is all lower‑case.
    """
    # 1. Split, lower‑case and deduplicate
    unique_words = {word.lower() for word in sentence.split()}

    # 2. Sort by (length, word) – Python's tuple ordering does exactly that
    sorted_words = sorted(unique_words, key=lambda w: (len(w), w))

    return sorted_words
```