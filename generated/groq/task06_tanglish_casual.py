```python
def sum_even_numbers(nums):
    """
    Return the sum of all even numbers in the given list.
    If there are no even numbers, return 0.

    Parameters:
        nums (list[int]): List of integers.

    Returns:
        int: Sum of even integers.
    """
    return sum(n for n in nums if n % 2 == 0)
```