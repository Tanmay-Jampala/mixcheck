```python
def missing_number(nums):
    """
    Return the missing whole number from 1..n given a list that contains all
    numbers except one, in any order.

    Example:
        missing_number([3, 1, 4])  # returns 2
    """
    n = len(nums) + 1               # the full range size
    expected_sum = n * (n + 1) // 2 # sum of 1..n
    return expected_sum - sum(nums)
```