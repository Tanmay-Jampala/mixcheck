```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    first = second = None
    for n in nums:
        if first is None or n > first:
            second = first
            first = n
        elif second is None or n > second:
            second = n
    return second
```