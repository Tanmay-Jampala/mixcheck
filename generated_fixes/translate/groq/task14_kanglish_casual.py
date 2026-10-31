Here’s a concise implementation of `are_anagrams`. It assumes the inputs are already lowercase strings containing only alphabetic characters, but it will still work correctly for any strings.

```python
def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` are anagrams of each other,
    i.e., they contain exactly the same letters with the same frequencies.

    Parameters
    ----------
    word1 : str
        First word (expected to be lowercase).
    word2 : str
        Second word (expected to be lowercase).

    Returns
    -------
    bool
        True if the two words are anagrams, False otherwise.
    """
    # Quick length check – if the lengths differ they cannot be anagrams.
    if len(word1) != len(word2):
        return False

    # Count the occurrences of each character in both words.
    # Using Python's built‑in `collections.Counter` makes this very clear.
    from collections import Counter
    return Counter(word1) == Counter(word2)


# Example usage
if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))   # True
    print(are_anagrams("hello", "world"))    # False
    print(are_anagrams("anagram", "nagaram"))# True
```

**Explanation**

1. **Length check** – If the two strings have different lengths, they can’t be anagrams, so we return `False` immediately.
2. **Counting letters** – `collections.Counter` creates a dictionary‑like object where each key is a character and each value is the number of times that character appears in the string.
3. **Comparison** – Two `Counter` objects are equal exactly when they have the same keys with the same counts, which is precisely the definition of an anagram.

Feel free to adapt the function (e.g., to ignore spaces or punctuation) by preprocessing the inputs before the length check.