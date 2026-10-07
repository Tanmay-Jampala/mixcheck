```python
def sum_even_numbers(numbers):
    """Return the sum of all even integers in the given list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: Sum of even numbers, or 0 if none are present.
    """
    return sum(num for num in numbers if num % 2 == 0)
```