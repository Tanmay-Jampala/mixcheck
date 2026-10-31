**Python – `sort_words`**

```python
def sort_words(sentence: str) -> list[str]:
    """
    Return a list of the unique words that appear in *sentence*.

    * The sentence is assumed to contain only words separated by a single
      space – no punctuation.
    * Words are compared case‑insensitively, but the returned words are
      all lower‑case.
    * The result is sorted first by word length (ascending) and, for words
      of the same length, alphabetically.
    * If *sentence* is an empty string, an empty list is returned.

    Parameters
    ----------
    sentence : str
        The input sentence.

    Returns
    -------
    list[str]
        Sorted list of unique, lower‑case words.
    """
    # 1. Empty sentence → empty list
    if not sentence:
        return []

    # 2. Split on spaces, convert to lower‑case
    words = [w.lower() for w in sentence.split()]

    # 3. Keep only unique words
    unique_words = sorted(set(words))

    # 4. Sort by length, then alphabetically
    unique_words.sort(key=lambda w: (len(w), w))

    return unique_words
```

### Example usage

```python
>>> sort_words("Apple banana apple Cherry")
['apple', 'banana', 'cherry']

>>> sort_words("")
[]
```

The function follows the requirements:

1. **Case‑insensitive uniqueness** – `set(words)` removes duplicates regardless of case.
2. **Lower‑case output** – all words are converted to lower‑case before processing.
3. **Sorting** – `key=lambda w: (len(w), w)` sorts first by length, then alphabetically.
4. **Empty input** – returns an empty list when the sentence is empty.