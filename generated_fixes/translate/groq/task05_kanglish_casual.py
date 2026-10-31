Here’s a compact, well‑documented implementation that meets all of the requirements:

```python
def remove_duplicates(seq):
    """
    Return a new list containing the elements of *seq* with duplicates removed.

    - Only the **first** occurrence of each value is kept.
    • The original order of elements is preserved.
    • The input sequence is **not** modified; a brand‑new list is returned.

    Parameters
    ----------
    seq : iterable
        Any iterable (list, tuple, generator, etc.) whose items are hashable.

    Returns
    -------
    list
        A list with duplicates removed while preserving order.

    Example
    -------
    >>> remove_duplicates([3, 5, 2, 3, 5, 7, 2])
    [3, 5, 2, 7]
    """
    seen = set()          # stores items we have already encountered
    result = []           # the list we will return

    for item in seq:
        if item not in seen:
            seen.add(item)   # mark it as seen
            result.append(item)

    return result
```

**How it works**

1. A `set` called `seen` tracks which values have already been encountered – look‑ups in a set are O(1).
2. We iterate over the original sequence once.
3. If the current `item` isn’t in `seen`, we add it to both `seen` and the `result` list.
4. Finally, `result` (a brand‑new list) is returned, leaving the original `seq` untouched.

This satisfies:
- **Duplicate removal** – each value appears only once.
- **First occurrence kept** – the first time a value appears it’s added; later repeats are ignored.
- **Order preservation** – items are appended to `result` in the order they’re encountered.
- **New list return** – the function never mutates the input.