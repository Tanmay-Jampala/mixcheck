```python
def missing_number(nums):
    """
    Return the missing integer from a list containing all whole numbers
    from 1 to n except one, in any order.
    """
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)
```