```python
def find_largest(numbers):
    """
    Return the largest number in the list, or None if the list is empty.
    
    Args:
        numbers (list): A list of numeric values.
    
    Returns:
        The largest number, or None if the list is empty.
    """
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
```