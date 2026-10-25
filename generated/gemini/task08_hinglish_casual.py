```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    unique_nums = sorted(list(set(nums)))
    return unique_nums[-2] if len(unique_nums) >= 2 else None
```