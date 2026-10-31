**Python function**

```python
def sort_words(sentence: str) -> list[str]:
    """
    Return a list of the unique words in *sentence* (case‑insensitive),
    all in lowercase, sorted first by word length (ascending) and then
    alphabetically for words of the same length.

    Parameters
    ----------
    sentence : str
        A sentence that contains words separated by a single space.
        No punctuation is expected.

    Returns
    -------
    list[str]
        The sorted list of unique words.  If *sentence* is empty or only
        whitespace, an empty list is returned.
    """
    # 1. Empty‑sentence guard
    if not sentence or sentence.strip() == "":
        return []

    # 2. Split on spaces, convert to lowercase, keep unique words
    words = {w.lower() for w in sentence.split()}

    # 3. Sort by length, then alphabetically
    return sorted(words, key=lambda w: (len(w), w))
```

**Examples**

```python
>>> sort_words("Apple banana apple")
['apple', 'banana']

>>> sort_words("Cat dog elephant")
['cat', 'dog', 'elephant']

>>> sort_words("")
[]
```

The function treats `"Apple"` and `"apple"` as the same word, returns the lowercase form, and sorts according to the rules you specified.