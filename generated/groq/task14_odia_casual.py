```python
from collections import Counter

def are_anagrams(word1: str, word2: str) -> bool:
    """Return True if the two lowercase words are anagrams, else False."""
    return Counter(word1) == Counter(word2)
```