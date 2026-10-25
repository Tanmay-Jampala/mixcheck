```python
def missing_number(nums):
    n = len(nums) + 1
    return (n * (n + 1) // 2) - sum(nums)
```