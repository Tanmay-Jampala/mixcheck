```python
def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` contain exactly the same letters
    with the same frequencies, otherwise False.
    Both inputs are assumed to be lowercase alphabetic strings.
    """
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)
```