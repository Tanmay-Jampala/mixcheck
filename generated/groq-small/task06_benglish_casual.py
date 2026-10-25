```python
def sum_even_numbers(numbers):
    """
    Return the sum of all even integers in the given list.
    If the list contains no even numbers, returns 0.
    """
    return sum(n for n in numbers if n % 2 == 0)
```