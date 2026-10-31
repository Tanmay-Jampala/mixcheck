Here’s a compact, self‑contained implementation that:

* Returns `1` for `n == 0` (the definition of 0!).
* Raises a `ValueError` for negative inputs (factorial is undefined for negative integers).
* Uses an iterative loop for efficiency and to avoid recursion limits.

```python
def factorial(n: int) -> int:
    """
    Return the factorial of a non‑negative integer n.

    Parameters
    ----------
    n : int
        The number to compute the factorial of. Must be >= 0.

    Returns
    -------
    int
        The factorial of n (n!).

    Raises
    ------
    ValueError
        If n is negative.

    Examples
    --------
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(-3)
    Traceback (most recent call last):
        ...
    ValueError: factorial is not defined for negative integers
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

You can test it directly:

```python
print(factorial(0))   # 1
print(factorial(5))   # 120
```

Feel free to integrate this function into your project or adapt it for larger numbers (e.g., using `math.prod` or a memoization strategy).