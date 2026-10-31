Here’s a compact, well‑documented implementation that satisfies all the requirements:

```python
def remove_duplicates(seq):
    """
    Return a new list containing the elements of *seq* with duplicates removed.
    
    The first occurrence of each element is kept, and the original order is
    preserved.  The function works for any iterable, but the return type is
    always a list.

    Parameters
    ----------
    seq : Iterable
        The input sequence (e.g. list, tuple, string, etc.).

    Returns
    -------
    list
        A new list with duplicates removed, preserving the original order.

    Examples
    --------
    >>> remove_duplicates([1, 2, 3, 2, 1, 4])
    [1, 2, 3, 4]

    >>> remove_duplicates('abracadabra')
    ['a', 'b', 'r', 'c', 'd']
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### Why this works

1. **`seen` set** – keeps track of elements that have already appeared.  
2. **`result` list** – collects the first occurrence of each element.  
3. The loop iterates over the input in its original order, so the order is preserved.  
4. Because we only add an element to `result` when it’s not in `seen`, duplicates are discarded.

Feel free to copy‑paste this into your project or adapt it to your specific needs!