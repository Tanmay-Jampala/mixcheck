```python
def remove_duplicates(seq):
    """Return a new list with duplicates removed, preserving the original order."""
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```