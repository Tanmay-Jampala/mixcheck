```python
def missing_number(arr):
    """
    Returns the missing number from a list containing all integers from 1 to n
    except one, where n = len(arr) + 1. The list can be in any order.
    """
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)
```