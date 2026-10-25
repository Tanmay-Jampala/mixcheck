```python
def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` are anagrams of each other.
    Both words are assumed to be lowercase alphabetic strings.
    """
    # Quick length check – if lengths differ they can't be anagrams
    if len(word1) != len(word2):
        return False

    # Count characters using a dictionary (or collections.Counter)
    counts = {}

    for ch in word1:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in word2:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False

    # All counts should be zero now
    return all(v == 0 for v in counts.values())
```