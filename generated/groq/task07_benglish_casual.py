```python
def factorial(n: int) -> int:
    """Return n! for a non‑negative integer n (0! = 1)."""
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```