```python
from collections import Counter


def are_anagrams(word1, word2):
    return Counter(word1) == Counter(word2)
```