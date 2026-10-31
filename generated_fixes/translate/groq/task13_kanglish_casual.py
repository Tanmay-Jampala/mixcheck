Here’s a compact, self‑contained implementation that follows the requirements:

```python
def word_count(sentence: str) -> dict[str, int]:
    """
    Count the occurrences of each word in a lowercase, space‑separated sentence.

    Parameters
    ----------
    sentence: str
        A string that contains only lowercase letters and single spaces
        between words (no punctuation).

    Returns
    -------
    dict[str, int]
        Mapping from each distinct word to the number of times it appears.
    """
    # Split the sentence into its individual words.
    # Using `split()` without arguments also handles leading/trailing spaces,
    # but the specification says there is exactly one space between words,
    # so `sentence.split(' ')` works as well.
    words = sentence.split()

    # Build the frequency dictionary.
    freq: dict[str, int] = {}
    for w in words:
        # Increment the count for the current word.
        freq[w] = freq.get(w, 0) + 1

    return freq


# ----------------------------------------------------------------------
# Example usage
if __name__ == "__main__":
    test_sentence = "the quick brown fox jumps over the lazy dog the the"
    print(word_count(test_sentence))
    # Output: {'the': 4, 'quick': 1, 'brown': 1, 'fox': 1,
    #          'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

**Explanation**

1. `sentence.split()` turns the input string into a list of words.
2. We iterate over that list, updating a dictionary (`freq`) where each key is a word and the value is its running total.
3. `dict.get(word, 0)` returns the current count for `word` (or `0` if it hasn’t been seen yet), allowing us to increment it in one line.

The function assumes the input meets the stated constraints (lower‑case, no punctuation, single spaces), so no extra cleaning is performed. If you ever need to handle more relaxed input, you could add preprocessing steps (e.g., `sentence.lower().strip()` and `re.sub(r'[^a-z\s]', '', sentence)`).