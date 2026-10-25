```python
def are_anagrams(word1: str, word2: str) -> bool:
    """Return True if word1 and word2 are anagrams of each other."""
    return sorted(word1) == sorted(word2)
```