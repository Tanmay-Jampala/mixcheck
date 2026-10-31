Sure!  
Below is a compact, idiomatic Python function that checks whether two **lower‑case** words are anagrams of each other.  
It returns `True` if they contain exactly the same letters with the same multiplicity, otherwise `False`.

```python
from collections import Counter

def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if word1 and word2 are anagrams of each other.
    
    Parameters
    ----------
    word1 : str
        First word (must be lowercase).
    word2 : str
        Second word (must be lowercase).
    
    Returns
    -------
    bool
        True if the words are anagrams, False otherwise.
    """
    # Quick length check – anagrams must have the same length
    if len(word1) != len(word2):
        return False

    # Count the occurrences of each character in both words
    return Counter(word1) == Counter(word2)
```

### Why this works

* `Counter` builds a dictionary of `{char: count}` for each word.  
* Two words are anagrams iff these dictionaries are identical.  
* The length check short‑circuits the comparison for words of different lengths, saving a bit of time.

### Usage examples

```python
print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pabble"))   # False
print(are_anagrams("abc", "abcd"))       # False
```

### Alternative (sorting) – if you prefer a one‑liner

```python
def are_anagrams_sort(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)
```

Both approaches are O(n log n) due to sorting or O(n) for the `Counter` method.  
Pick the one you find clearer or faster for your use case. Happy coding!