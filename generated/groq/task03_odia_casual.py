```python
def find_largest(nums: list[float]) -> float | None:
    """Return the largest number in `nums` or None if the list is empty."""
    if not nums:
        return None
    max_val = nums[0]
    for n in nums[1:]:
        if n > max_val:
            max_val = n
    return max_val
```