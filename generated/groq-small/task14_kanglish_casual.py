Sure!  
Below is a compact, production‑ready implementation of `are_anagrams` that works for two **lower‑case** strings.  
It returns `True` if the two words contain exactly the same letters the same number of times, otherwise `False`.

```python
from collections import Counter

def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if word1 and word2 are anagrams of each other.
    Both arguments must be lowercase alphabetic strings.

    Parameters
    ----------
    word1 : str
        First word (lower‑case).
    word2 : str
        Second word (lower‑case).

    Returns
    -------
    bool
        True if the words are anagrams, False otherwise.
    """
    # Quick length check – anagrams must have the same length
    if len(word1) != len(word2):
        return False

    # Count the occurrences of each letter in both words
    return Counter(word1) == Counter(word2)
```

### How it works

1. **Length check** – If the words differ in length they cannot be anagrams, so we return `False` immediately.
2. **Counting letters** – `collections.Counter` builds a dictionary of `{letter: count}` for each word.
3. **Comparison** – Two words are anagrams iff their counters are equal.

### Usage example

```python
>>> are_anagrams("listen", "silent")
True
>>> are_anagrams("hello", "world")
False
>>> are_anagrams("abc", "cba")
True
```

### Alternative (sorting) – if you prefer not to import `Counter`

```python
def are_anagrams_sort(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)
```

Both versions give the same result; the `Counter` approach is usually faster for longer strings because it runs in linear time, whereas sorting is \(O(n \log n)\).  

Feel free to drop the function into your project and call it whenever you need to check for anagrams!