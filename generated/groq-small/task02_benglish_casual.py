```python
def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the string `s`,
    counting both lowercase and uppercase letters."""
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)
```