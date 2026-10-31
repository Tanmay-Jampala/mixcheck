```python
def sort_words(sentence: str) -> list[str]:
    """
    Return the unique words from *sentence* in lowercase, sorted first by word length
    (ascending) and then alphabetically for words of the same length.

    Parameters
    ----------
    sentence : str
        A sentence containing words separated by a single space.  No punctuation
        is present.  The function is tolerant of an empty string.

    Returns
    -------
    list[str]
        A list of the unique words in lowercase, sorted as described.

    Examples
    --------
    >>> sort_words("Hello world hello")
    ['hello', 'world']

    >>> sort_words("")
    []

    >>> sort_words("Banana apple")
    ['apple', 'banana']
    """
    # If the sentence is empty (or only whitespace) return an empty list
    if not sentence:
        return []

    # Split on spaces, lower‑case each word, and keep only unique ones
    unique_words = {word.lower() for word in sentence.split()}

    # Sort by length first, then alphabetically
    return sorted(unique_words, key=lambda w: (len(w), w))
```

**Explanation**

1. **Empty sentence** – If `sentence` is falsy (empty string, `None`, etc.) we return an empty list immediately.
2. **Splitting & lower‑casing** – `sentence.split()` splits on whitespace.  
   Each word is converted to lowercase and added to a set to guarantee uniqueness.
3. **Sorting** – `sorted()` uses a key that is a tuple: `(len(word), word)`.  
   Python sorts tuples lexicographically, so words are first ordered by length, then alphabetically.
4. **Return** – The sorted list is returned.