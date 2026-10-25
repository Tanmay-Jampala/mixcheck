```python
def missing_number(nums):
    """
    Given a list `nums` containing all integers from 1 to n with exactly one missing,
    return the missing integer. The order of elements in `nums` is arbitrary.
    """
    n = len(nums) + 1                     # the expected length including the missing number
    expected_sum = n * (n + 1) // 2       # sum of 1..n
    actual_sum = sum(nums)                # sum of the given numbers
    return expected_sum - actual_sum
```