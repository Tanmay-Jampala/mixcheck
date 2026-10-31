```python
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed).
    
    Args:
        n: Non‑negative integer where fibonacci(0)=0 and fibonacci(1)=1.
    
    Returns:
        The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```