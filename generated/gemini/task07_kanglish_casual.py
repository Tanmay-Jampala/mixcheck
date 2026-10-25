```python
def factorial(n):
    if n < 0:
        return "Negative numbersge factorial illa"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```