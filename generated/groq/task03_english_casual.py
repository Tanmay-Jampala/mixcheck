```python
def find_largest(numbers):
    """
    Return the largest number in the list `numbers`.
    If the list is empty, return None.
    """
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
```