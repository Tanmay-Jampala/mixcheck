```python
def find_largest(nums):
    if not nums:
        return None
    largest = nums[0]
    for n in nums[1:]:
        if n > largest:
            largest = n
    return largest
```