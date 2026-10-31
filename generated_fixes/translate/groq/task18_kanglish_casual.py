Here is a compact, well‑documented implementation that follows the specification:

```python
def sort_words(sentence: str) -> list[str]:
    """
    Return the unique words of *sentence* in lowercase, sorted
    first by length (shortest to longest) and then alphabetically
    for words of equal length.

    The input sentence is assumed to contain only words separated by a
    single space and no punctuation.  Capitalisation is ignored – “Apple”
    and “apple” are treated as the same word.

    Parameters
    ----------
    sentence: str
        The sentence to process.  An empty string yields an empty list.

    Returns
    -------
    list[str]
        Sorted list of unique, lower‑cased words.
    """
    # Guard against the empty‑string case early
    if not sentence:
        return []

    # 1. Split on the single space delimiter.
    # 2. Normalise every word to lower‑case.
    # 3. Use a set to keep only unique words.
    unique_words = {word.lower() for word in sentence.split(' ')}

    # Sort by a tuple (length, word) – Python sorts tuples lexicographically,
    # so length is the primary key and the word itself is the secondary key.
    sorted_words = sorted(unique_words, key=lambda w: (len(w), w))

    return sorted_words


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    examples = [
        "The quick brown fox jumps over the lazy dog",
        "Hello hello HELLO world WORLD",
        "",
        "a aa aaa aaaa aaaa aa a"
    ]

    for s in examples:
        print(f"Input : {s!r}")
        print(f"Output: {sort_words(s)}\n")
```

### How it works
1. **Empty check** – `if not sentence:` returns `[]` immediately for an empty input.
2. **Tokenisation & normalisation** – `sentence.split(' ')` yields the words; the set‑comprehension `{word.lower() for word in …}` lower‑cases each word and automatically discards duplicates.
3. **Sorting** – `sorted(..., key=lambda w: (len(w), w))` orders the words by the tuple `(length, word)`.  
   * The first element (`len(w)`) ensures shorter words come first.  
   * The second element (`w`) resolves ties alphabetically.
4. The resulting list is returned.

The function meets all the requirements: it handles case‑insensitivity, removes duplicates, respects the length‑then‑alphabetical ordering, and returns an empty list for an empty sentence.