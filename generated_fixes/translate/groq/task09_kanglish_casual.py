Here’s a compact, well‑documented implementation. It treats any sequence of one or more whitespace characters as a separator, so leading, trailing, or multiple spaces between words are ignored automatically.

```python
def count_words(text: str) -> int:
    """
    Return the number of words in *text*.

    A word is defined as a maximal sequence of non‑whitespace characters.
    Consecutive spaces (or any other whitespace such as tabs / newlines) are
    treated as a single separator, and leading/trailing whitespace is ignored.

    Parameters
    ----------
    text : str
        The string to be examined.

    Returns
    -------
    int
        The count of words found in *text*.

    Examples
    --------
    >>> count_words("Hello world")
    2
    >>> count_words("   leading and trailing   ")
    3
    >>> count_words("multiple   spaces   between")
    3
    >>> count_words("")
    0
    """
    # str.split() without an argument splits on any whitespace and discards
    # empty strings, which is exactly the behaviour we need.
    return len(text.split())
```

**How it works**

- `text.split()` (with no arguments) splits the string on *any* whitespace (`' '`, `'\t'`, `'\n'`, …) and automatically removes empty results that would arise from consecutive separators.
- `len(...)` then gives the number of resulting substrings, i.e., the number of words.

You can use the function directly:

```python
sentence = "  The quick   brown fox jumps   over the lazy dog  "
print(count_words(sentence))   # → 9
```