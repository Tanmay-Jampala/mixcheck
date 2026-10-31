**Python function – `count_words`**

```python
def count_words(text: str) -> int:
    """
    Return the number of words in *text*.

    • Words are separated by one or more spaces.
    • Leading, trailing and consecutive spaces are ignored.
    • An empty string (or a string that contains only spaces) returns 0.

    Parameters
    ----------
    text : str
        The input string.

    Returns
    -------
    int
        Number of words found.
    """
    # `split()` without an argument splits on any whitespace and
    # automatically discards empty parts caused by extra spaces.
    words = text.split()
    return len(words)


# -------------------------------------------------
# Example usage
if __name__ == "__main__":
    examples = [
        "hello world",                     # 2
        "  leading space",                 # 2
        "trailing space   ",               # 2
        "  multiple   spaces  inside  ",   # 3
        "",                                # 0
        "    ",                            # 0
        "one",                             # 1
    ]

    for s in examples:
        print(f"'{s}' → {count_words(s)} word(s)")
```

### How it works
1. **`text.split()`**  
   - When called **without an argument**, `split()` treats **any consecutive whitespace** (spaces, tabs, newlines) as a single separator.  
   - It also **drops empty strings** that would appear because of leading, trailing, or multiple spaces.

2. The resulting list `words` contains only the actual words, so `len(words)` is the exact count.

### Quick test in the REPL

```python
>>> count_words("  python   is   fun  ")
3
>>> count_words("")
0
>>> count_words("single")
1
```

Feel free to copy the function into your project; it works for any Unicode string and respects the usual definition of “words separated by spaces”.