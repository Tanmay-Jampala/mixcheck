```python
def sum_even_numbers(nums):
    """
    Return the sum of all even numbers in the given list.
    If there are no even numbers, returns 0.

    :param nums: List[int] – list of integers
    :return: int – sum of even integers
    """
    return sum(n for n in nums if n % 2 == 0)
```