```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    return sorted(nums)[-2]
```