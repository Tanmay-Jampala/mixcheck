```python
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```