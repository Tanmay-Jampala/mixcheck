```python
def missing_number(nums):
    """
    Return the missing number from a list that should contain all integers
    from 1 to n exactly once, with exactly one number missing.
    
    Parameters
    ----------
    nums : list[int]
        List of integers in any order, length n-1 where the full range is 1..n.
    
    Returns
    -------
    int
        The missing integer.
    """
    n = len(nums) + 1                     # the full size should be n
    expected_sum = n * (n + 1) // 2       # sum of 1..n
    actual_sum = sum(nums)                # sum of given numbers
    return expected_sum - actual_sum
```