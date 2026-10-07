```python
def missing_number(nums):
    n = len(nums) + 1               # total numbers should be n
    expected_sum = n * (n + 1) // 2 # sum of 1..n
    return expected_sum - sum(nums)
```