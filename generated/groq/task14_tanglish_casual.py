```python
def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` are anagrams of each other.
    Both inputs are assumed to be lowercase alphabetic strings.
    """
    return sorted(word1) == sorted(word2)
```