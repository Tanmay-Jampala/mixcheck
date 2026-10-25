```python
def missing_number(nums):
    """
    Given a list `nums` containing all integers from 1 to n except one,
    return the missing integer. The order of elements is arbitrary.
    """
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)
```