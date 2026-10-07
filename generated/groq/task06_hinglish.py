```python
def sum_even_numbers(nums):
    """Return the sum of even numbers in the given list.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: Sum of even numbers, or 0 if there are none.
    """
    return sum(num for num in nums if num % 2 == 0)
```