```python
def sum_even_numbers(nums):
    """Return the sum of even numbers in the list `nums`.
    If there are no even numbers, return 0.
    """
    return sum(n for n in nums if n % 2 == 0)
```