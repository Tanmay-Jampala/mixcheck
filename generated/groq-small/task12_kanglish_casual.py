**Python – `capitalize_words` function**

```python
def capitalize_words(sentence: str) -> str:
    """
    Takes a sentence that is entirely in lowercase and has words separated by a single space.
    Returns the sentence with the first letter of each word capitalised.

    Parameters
    ----------
    sentence : str
        The input sentence (e.g. "hello world from python").

    Returns
    -------
    str
        The capitalised sentence (e.g. "Hello World From Python").
    """
    # Ensure we are working with a clean string
    sentence = sentence.strip()          # remove leading/trailing spaces
    if not sentence:
        return ""

    # Split on single spaces, capitalise each word, and re‑join
    capitalised = ' '.join(word.capitalize() for word in sentence.split(' '))
    return capitalised
```

### How it works

1. **Strip** – removes any accidental leading or trailing spaces.
2. **Split** – breaks the sentence into a list of words using the single space as a delimiter.
3. **Capitalize** – `str.capitalize()` turns the first character of each word to uppercase and lower‑cases the rest.
4. **Join** – recombines the words with a single space between them.

### Example usage

```python
>>> capitalize_words("hello world from python")
'Hello World From Python'

>>> capitalize_words("   this is a test   ")
'This Is A Test'
```

Feel free to drop this function into your project or adapt it to handle different delimiters or mixed‑case input if needed.