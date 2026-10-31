Here’s a compact, well‑documented implementation that follows the exact steps you described:

```python
import re

def capitalize_words(sentence: str) -> str:
    """
    Convert a sentence to “title case” with strict formatting.

    Steps performed:
    1. Convert the whole string to lower‑case.
    2. Collapse any run of whitespace characters (spaces, tabs, new‑lines, …)
       into a single ordinary space.
    3. Strip leading/trailing whitespace.
    4. Capitalise the first character of each word.

    Parameters
    ----------
    sentence: str
        The input text.  If ``None`` or an empty string is supplied, an empty
        string is returned.

    Returns
    -------
    str
        The cleaned, title‑cased sentence.

    Examples
    --------
    >>> capitalize_words("  HELLO   world!  ")
    'Hello World!'
    >>> capitalize_words("PYTHON\tis   awesome")
    'Python Is Awesome'
    """
    if not sentence:
        # Handles None, '' and other falsy values gracefully.
        return ""

    # 1️⃣ lower‑case everything
    lowered = sentence.lower()

    # 2️⃣ collapse any whitespace run to a single space
    #    ``re.sub`` is used because it also handles tabs, new‑lines, etc.
    collapsed = re.sub(r'\s+', ' ', lowered)

    # 3️⃣ strip leading/trailing spaces (they would otherwise become empty words)
    cleaned = collapsed.strip()

    # 4️⃣ title‑case each word.
    #    ``str.title()`` would also work, but it also lower‑cases characters
    #    after an apostrophe (e.g. "don't" → "Don'T").  Using ``str.capitalize``
    #    on each split word avoids that pitfall.
    result = ' '.join(word.capitalize() for word in cleaned.split(' '))

    return result
```

### Why not just `sentence.title()`?
`str.title()` blindly capitalises the character after *any* non‑alphabetic character, which can give surprising results such as:

```python
"don't stop".title()   # -> "Don'T Stop"
```

The implementation above:

* normalises whitespace with a regular expression,
* respects apostrophes and other punctuation,
* and still produces the desired “first‑letter‑uppercase, rest‑lowercase” output.