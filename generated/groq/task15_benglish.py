```python
def missing_number(nums):
    """
    Return the missing number from a list that should contain all integers
    from 1 to n exactly once, except one missing value.
    """
    n = len(nums) + 1               # because one number is missing
    expected_sum = n * (n + 1) // 2 # sum of 1..n
    return expected_sum - sum(nums)
```