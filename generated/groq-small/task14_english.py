```python
def are_anagrams(word1: str, word2: str) -> bool:
    """Return True if word1 and word2 are anagrams of each other."""
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)
```