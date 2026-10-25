```python
def second_largest(nums):
    """Return the second largest number in a list of distinct numbers.
    If the list has fewer than 2 elements, return None."""
    if len(nums) < 2:
        return None

    largest = second = None
    for n in nums:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif second is None or n > second:
            second = n
    return second
```