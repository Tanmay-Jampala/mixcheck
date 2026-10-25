```python
def missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)
```