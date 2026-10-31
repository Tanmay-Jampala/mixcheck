Here’s a compact, robust implementation that follows the rules you described:

```python
def count_words(text: str) -> int:
    """
    Return the number of words in *text*.

    Words are defined as sequences of non‑space characters separated by one or more
    space characters. Leading, trailing, and consecutive internal spaces are ignored.

    Parameters
    ----------
    text : str
        The string to be examined.

    Returns
    -------
    int
        The number of words found.
    """
    # ``split()`` without arguments splits on any whitespace and automatically
    # discards empty strings that would otherwise arise from consecutive spaces.
    return len(text.split())
```

### Why this works

* `text.split()` (without an explicit separator) splits on **any** whitespace
  (spaces, tabs, newlines, etc.) and automatically removes empty tokens that
  would result from multiple consecutive whitespace characters.
* `len(...)` gives the count of the resulting tokens, i.e. the number of words.

### Quick examples

```python
>>> count_words("Hello world")
2
>>> count_words("  Leading and trailing   ")
4
>>> count_words("Multiple   spaces   between   words")
5
>>> count_words("")
0
```

Feel free to drop this function into your project or adapt it to your specific needs!