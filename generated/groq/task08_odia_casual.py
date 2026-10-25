```python
def second_largest(nums):
    """Return the second largest distinct number in the list, or None if it doesn't exist."""
    distinct = set(nums)
    if len(distinct) < 2:
        return None
    # Remove the largest element and return the next one
    distinct.remove(max(distinct))
    return max(distinct)
```