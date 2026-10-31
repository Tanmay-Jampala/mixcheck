```python
def missing_number(nums):
    """
    Return the missing integer from a list that should contain all numbers
    from 1 to n exactly once, where one number is omitted.
    
    Parameters
    ----------
    nums : list[int]
        List of distinct integers in the range [1, n] with exactly one missing.
        The order of elements is arbitrary.
    
    Returns
    -------
    int
        The missing number.
    """
    n = len(nums) + 1               # because one number is missing
    expected_sum = n * (n + 1) // 2 # sum of 1..n
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```