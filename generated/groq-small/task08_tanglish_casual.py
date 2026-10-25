```python
def second_largest(nums):
    # Remove duplicates and sort in descending order
    unique_nums = sorted(set(nums), reverse=True)
    # Return the second element if it exists, otherwise None
    return unique_nums[1] if len(unique_nums) >= 2 else None
```