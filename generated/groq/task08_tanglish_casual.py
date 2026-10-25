```python
def second_largest(nums):
    """
    Return the second largest distinct number in the list `nums`.
    If there are fewer than two distinct numbers, return None.
    """
    # Use a set to keep only distinct values
    distinct = set(nums)
    if len(distinct) < 2:
        return None

    # Remove the largest element, then return the new max
    distinct.remove(max(distinct))
    return max(distinct)
```