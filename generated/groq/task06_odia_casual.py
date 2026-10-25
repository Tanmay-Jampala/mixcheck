```python
def sum_even_numbers(nums):
    """Return the sum of even numbers in the list `nums`. Returns 0 if none."""
    return sum(x for x in nums if x % 2 == 0)
```