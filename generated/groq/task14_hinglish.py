```python
def are_anagrams(word1: str, word2: str) -> bool:
    """Return True if `word1` and `word2` are anagrams (same letters with same counts)."""
    return sorted(word1) == sorted(word2)
```