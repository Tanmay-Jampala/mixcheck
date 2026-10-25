```python
def missing_number(nums):
    """
    Given a list `nums` that contains every integer from 1 to n exactly once
    except for one missing value, return that missing integer.
    """
    n = len(nums) + 1               # the original length including the missing number
    expected_sum = n * (n + 1) // 2 # sum of 1..n
    return expected_sum - sum(nums)
```