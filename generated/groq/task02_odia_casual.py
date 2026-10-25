```python
def count_vowels(s: str) -> int:
    return sum(1 for ch in s if ch.lower() in "aeiou")
```