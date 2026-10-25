```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]
```