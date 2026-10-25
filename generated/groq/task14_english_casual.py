```python
from collections import Counter

def are_anagrams(word1: str, word2: str) -> bool:
    """Return True if `word1` and `word2` contain the same letters
    with the same frequencies (case‑sensitive, assumes lowercase input)."""
    return Counter(word1) == Counter(word2)
```