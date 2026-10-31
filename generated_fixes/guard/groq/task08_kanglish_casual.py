```python
def second_largest(nums):
    """
    Return the second largest distinct number in the list `nums`.
    If the list contains fewer than two distinct numbers, return None.
    """
    # Use a set to keep only distinct values
    distinct = set(nums)
    if len(distinct) < 2:
        return None

    # Remove the largest element, then the max of the remaining set is the second largest
    distinct.remove(max(distinct))
    return max(distinct)
```