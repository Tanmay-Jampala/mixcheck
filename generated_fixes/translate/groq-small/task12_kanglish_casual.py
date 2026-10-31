Here’s a compact, self‑contained Python function that does exactly what you described:

```python
def capitalize_words(sentence: str) -> str:
    """
    Capitalize the first letter of every word in a fully‑lowercase sentence.

    Parameters
    ----------
    sentence : str
        A string that is guaranteed to be all lowercase and to contain words
        separated by a single space (no leading/trailing spaces, no multiple
        spaces).

    Returns
    -------
    str
        The sentence with the first letter of each word capitalized.
    """
    # Split on the single space, capitalize each part, then re‑join.
    return ' '.join(word.capitalize() for word in sentence.split(' '))
```

### Why this works

1. **`sentence.split(' ')`**  
   Splits the string into a list of words. Because the input guarantees a single space between words, this is safe and fast.

2. **`word.capitalize()`**  
   The built‑in `str.capitalize()` method turns the first character into uppercase and the rest into lowercase. Since the input is already all lowercase, this is exactly what we need.

3. **`' '.join(...)`**  
   Re‑assembles the list of capitalized words back into a single string with single spaces.

### Example usage

```python
>>> capitalize_words("the quick brown fox jumps over the lazy dog")
'The Quick Brown Fox Jumps Over The Lazy Dog'
```

### Edge cases handled

| Input | Output |
|-------|--------|
| `""` | `""` |
| `"a"` | `"A"` |
| `"multiple   spaces"` | (not allowed by spec – would raise an error or produce unintended results) |

If you ever need to support inputs that might contain leading/trailing spaces or multiple spaces between words, you can tweak the function:

```python
def capitalize_words_strict(sentence: str) -> str:
    words = sentence.strip().split()
    return ' '.join(word.capitalize() for word in words)
```

But for the exact constraints you gave, the first version is the most efficient. Happy coding!