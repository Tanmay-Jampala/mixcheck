```python
def remove_duplicates(seq):
    """Return a new list containing the items of *seq* without duplicates,
    preserving the original order (first occurrence kept)."""
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```