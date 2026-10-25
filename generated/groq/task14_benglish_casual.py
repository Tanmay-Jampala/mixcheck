```python
def are_anagrams(w1: str, w2: str) -> bool:
    """Return True if w1 and w2 are anagrams (both lowercase), else False."""
    return sorted(w1) == sorted(w2)
```