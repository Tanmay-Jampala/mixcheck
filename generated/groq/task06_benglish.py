```python
def sum_even_numbers(nums):
    """Return the sum of even numbers in the given list.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: Sum of all even numbers; 0 if none are present.
    """
    return sum(n for n in nums if n % 2 == 0)
```