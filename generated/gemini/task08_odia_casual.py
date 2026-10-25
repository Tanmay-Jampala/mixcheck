```python
def second_largest(lst):
    unique_nums = list(set(lst))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]
```