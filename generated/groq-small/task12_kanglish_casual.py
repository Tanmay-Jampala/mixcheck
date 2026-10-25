Sure!  
Here’s a tiny, self‑contained Python function that does exactly what you described:

```python
def capitalize_words(sentence: str) -> str:
    """
    Takes a sentence that is entirely in lowercase and has words separated by a single space.
    Returns the same sentence but with the first letter of each word capitalised.

    Parameters
    ----------
    sentence : str
        The input sentence (e.g. "hello world from python").

    Returns
    -------
    str
        The capitalised sentence (e.g. "Hello World From Python").
    """
    # Guard against an empty string – split() would return [] and join() would give '' anyway,
    # but this makes the intent crystal‑clear.
    if not sentence:
        return ""

    # Split on spaces, capitalize each word, then re‑join with a single space.
    return " ".join(word.capitalize() for word in sentence.split(" "))
```

### Quick demo

```python
>>> capitalize_words("hello world from python")
'Hello World From Python'

>>> capitalize_words("this is a test")
'This Is A Test'

>>> capitalize_words("")          # empty input
''
```

### Why this works

* `sentence.split(" ")` splits the string into a list of words using a single space as the delimiter.
* `word.capitalize()` turns the first character of each word into uppercase and leaves the rest unchanged.
* `" ".join(...)` stitches the capitalised words back together with a single space between them.

Feel free to drop this function into your project or tweak it if you need to handle punctuation, multiple spaces, or other edge cases!