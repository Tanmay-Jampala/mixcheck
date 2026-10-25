```python
def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = second = float('-inf')
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second:
            second = n
    return second
```