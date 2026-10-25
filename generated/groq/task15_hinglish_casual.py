```python
def missing_number(arr):
    """
    Return the missing number from a list that should contain all integers
    from 1 to n exactly once, with one number missing.
    """
    n = len(arr) + 1                     # because one number is missing
    expected_sum = n * (n + 1) // 2      # sum of 1..n
    return expected_sum - sum(arr)
```