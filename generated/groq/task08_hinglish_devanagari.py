```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    # Find the largest and second largest in one pass
    largest = second = None
    for n in nums:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif second is None or n > second:
            second = n
    return second
```