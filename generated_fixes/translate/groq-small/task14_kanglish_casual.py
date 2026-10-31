Here’s a compact, easy‑to‑read implementation that uses Python’s `collections.Counter` to compare the letter frequencies of the two words:

```python
from collections import Counter

def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` are anagrams of each other.

    Both arguments must be lowercase alphabetic strings.  The function
    compares the frequency of each letter in the two words; if the
    frequencies match exactly, the words are anagrams.

    Parameters
    ----------
    word1 : str
        First word to compare.
    word2 : str
        Second word to compare.

    Returns
    -------
    bool
        True if the words are anagrams, False otherwise.
    """
    # Quick length check – anagrams must be the same length
    if len(word1) != len(word2):
        return False

    # Count the letters in each word
    return Counter(word1) == Counter(word2)
```

### How it works

1. **Length check** – If the words differ in length, they can’t be anagrams, so we return `False` immediately.
2. **Counting letters** – `Counter` builds a dictionary mapping each letter to its count in the word.
3. **Comparison** – Two `Counter` objects are equal if they contain the same keys with the same counts, which is exactly the definition of an anagram.

### Example usage

```python
>>> are_anagrams("listen", "silent")
True
>>> are_anagrams("hello", "world")
False
>>> are_anagrams("aabbcc", "abcabc")
True
```

### Alternative (sorting) implementation

If you prefer not to import `Counter`, you can sort the strings instead:

```python
def are_anagrams_sort(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)
```

Both approaches run in O(n log n) time (sorting) or O(n) time (Counter) and use O(n) additional space. The `Counter` version is usually faster for longer strings because it only scans each string once.