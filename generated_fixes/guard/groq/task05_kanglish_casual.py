```python
def remove_duplicates(seq):
    """
    Return a new list containing the elements of `seq` with duplicates removed,
    preserving the original order of first occurrence.

    Parameters
    ----------
    seq : iterable
        The input sequence (e.g., list) that may contain duplicate items.

    Returns
    -------
    list
        A list with duplicates removed, maintaining the original order.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```