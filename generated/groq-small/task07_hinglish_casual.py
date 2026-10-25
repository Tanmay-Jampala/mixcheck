```python
def factorial(n: int) -> int:
    """Return the factorial of a non‑negative integer n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```