Here’s a simple Python function that takes a lowercase sentence (words separated by spaces) and returns a new string where the first letter of each word is capitalized:

```python
def capitalize_words(sentence: str) -> str:
    """
    Convert a lowercase sentence into title‑case.

    Parameters
    ----------
    sentence : str
        A string containing only lowercase letters and spaces
        (e.g. "this is a sample sentence").

    Returns
    -------
    str
        The same sentence with the first character of each word
        capitalized (e.g. "This Is A Sample Sentence").
    """
    # Split the sentence into individual words
    words = sentence.split()

    # Capitalize the first character of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the words back together with a single space
    return " ".join(capitalized_words)


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_sentence = "hello world this is python"
    result = capitalize_words(test_sentence)
    print(result)   # Output: "Hello World This Is Python"
```

### How it works
1. **`sentence.split()`** – breaks the input string into a list of words using whitespace as the delimiter.
2. **`word.capitalize()`** – returns a copy of the word with its first character in uppercase and the rest in lowercase. Since the input is already all lowercase, this gives the desired result.
3. **`" ".join(...)`** – stitches the list of capitalized words back together, inserting a single space between each word.

Feel free to drop this function into any script or module where you need to title‑case a lowercase sentence.