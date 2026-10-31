```python
def factorial(n: int) -> int:
    """
    Compute the factorial of a non‑negative integer n.

    Parameters
    ----------
    n : int
        The integer whose factorial is required. Must be >= 0.

    Returns
    -------
    int
        n! (the factorial of n). By definition, 0! == 1.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```