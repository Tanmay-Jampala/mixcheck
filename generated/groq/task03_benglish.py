```python
def find_largest(numbers):
    """
    Return the largest number in the given list.
    If the list is empty, return None.
    """
    if not numbers:          # empty list check
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
```