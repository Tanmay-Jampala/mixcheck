```python
def second_largest(nums):
    """
    Return the second largest number in the list `nums`.
    If the list has fewer than 2 elements, return None.
    Assumes all numbers are distinct.
    """
    if len(nums) < 2:
        return None

    # Keep track of the largest and second largest while scanning once
    largest, second = (nums[0], None) if nums[0] > nums[1] else (nums[1], nums[0])

    for n in nums[2:]:
        if n > largest:
            second, largest = largest, n
        elif second is None or n > second:
            second = n

    return second
```