Here’s a compact, self‑contained implementation that follows the exact requirements you listed:

```python
def word_count(sentence: str) -> dict:
    """
    Count the occurrences of each word in a lower‑cased, space‑separated sentence.

    Assumptions (as per the request):
    • The input is already lower‑cased.
    • No punctuation characters are present.
    • Words are separated by a **single** space.

    Parameters
    ----------
    sentence : str
        The sentence to analyse.

    Returns
    -------
    dict
        A dictionary where each key is a word and the corresponding value
        is the number of times that word appears in the sentence.
    """
    # If the sentence is empty we simply return an empty dict
    if not sentence:
        return {}

    # Split on the single space – this yields a list of words
    words = sentence.split(' ')

    # Build the frequency dictionary
    freq = {}
    for w in words:
        # Using dict.get saves an explicit `if` check
        freq[w] = freq.get(w, 0) + 1

    return freq


# -------------------------------------------------
# Example usage
if __name__ == "__main__":
    s = "the quick brown fox jumps over the lazy dog the the"
    # The sentence is already lower‑cased and has single spaces only
    result = word_count(s)
    print(result)
    # Output:
    # {'the': 4, 'quick': 1, 'brown': 1, 'fox': 1,
    #  'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

### How it works
1. **Early exit for an empty string** – returns `{}`.
2. `sentence.split(' ')` splits the string on the single space character, giving a list of words.
3. The loop updates a dictionary `freq` where `freq[w]` holds the count for word `w`.  
   `freq.get(w, 0)` returns the current count (or `0` if the word isn’t in the dict yet) and we add `1`.

The function meets all the constraints:

* **Lower‑cased input** – no conversion needed inside the function.  
* **No punctuation** – the split works directly.  
* **Single‑space separation** – `split(' ')` respects that.  
* **Returns a dictionary** mapping each word to its frequency.