```python
def are_anagrams(s1: str, s2: str) -> bool:
    """Return True if the two lowercase words are anagrams, else False."""
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
```