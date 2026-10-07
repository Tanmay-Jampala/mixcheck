```python
def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the given string, case‑insensitive."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)
```