```python
def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` contain exactly the same letters
    with the same frequencies, otherwise return False.
    Both inputs are assumed to be lowercase alphabetic strings.
    """
    # Quick length check – if lengths differ they can't be anagrams
    if len(word1) != len(word2):
        return False

    # Count characters using a dictionary (or collections.Counter)
    from collections import Counter
    return Counter(word1) == Counter(word2)


# Example usage:
# print(are_anagrams("listen", "silent"))  # True
```