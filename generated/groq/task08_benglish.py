```python
def second_largest(nums):
    """
    Return the second‑largest number in a list of distinct numbers.
    If the list has fewer than two elements, return None.
    """
    if len(nums) < 2:
        return None

    # Initialize the two largest values
    largest = second = None
    for n in nums:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif second is None or n > second:
            second = n
    return second
```