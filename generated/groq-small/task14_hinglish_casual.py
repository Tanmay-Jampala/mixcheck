```python
def are_anagrams(a: str, b: str) -> bool:
    """Return True if `a` and `b` are anagrams (same letters, same counts)."""
    return sorted(a) == sorted(b)
```