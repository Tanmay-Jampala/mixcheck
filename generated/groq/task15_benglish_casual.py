```python
def missing_number(nums):
    """
    Return the missing number from a list that should contain all integers
    from 1 to n exactly once, with exactly one number missing.
    """
    n = len(nums) + 1               # the expected size including the missing element
    expected_sum = n * (n + 1) // 2 # sum of 1..n
    return expected_sum - sum(nums)
```