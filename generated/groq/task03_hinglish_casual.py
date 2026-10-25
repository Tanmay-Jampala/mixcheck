```python
def find_largest(nums):
    """
    Return the largest number in the list `nums`.
    If the list is empty, return None.
    """
    if not nums:
        return None
    max_val = nums[0]
    for n in nums[1:]:
        if n > max_val:
            max_val = n
    return max_val
```