Here’s a simple Python function that does exactly that – it takes a lowercase sentence where the words are separated by a single space, capitalizes the first letter of each word, and returns the transformed string.

```python
def capitalize_words(sentence: str) -> str:
    """
    Capitalize the first letter of each word in a lowercase sentence.

    Parameters
    ----------
    sentence : str
        A string containing only lowercase letters and single spaces between words.

    Returns
    -------
    str
        The sentence with each word’s first character in uppercase.
    """
    # Split the sentence into words, capitalize each, then join back with spaces
    capitalized = ' '.join(word.capitalize() for word in sentence.split(' '))
    return capitalized


# Example usage
if __name__ == "__main__":
    s = "this is a sample sentence"
    print(capitalize_words(s))   # Output: "This Is A Sample Sentence"
```

**How it works**

1. `sentence.split(' ')` breaks the input string into a list of words using the single space as the delimiter.
2. The generator expression `word.capitalize() for word in ...` converts each word so that its first character becomes uppercase while the rest stay lowercase.
3. `' '.join(...)` stitches the capitalized words back together with a single space between them.
4. The resulting string is returned.

Feel free to drop this function into any script or module where you need this behavior.