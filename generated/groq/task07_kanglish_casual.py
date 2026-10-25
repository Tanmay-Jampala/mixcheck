Here’s a clean, well‑documented Python function that computes the factorial of a non‑negative integer.  

* If **n** is negative the function raises a `ValueError` (because factorial is undefined for negative integers).  
* By definition `0! = 1`.  

```python
def factorial(n: int) -> int:
    """
    Return the factorial of a non‑negative integer n.

    Parameters
    ----------
    n : int
        The number whose factorial is required. Must be >= 0.

    Returns
    -------
    int
        n!  (product of all positive integers ≤ n)

    Raises
    ------
    ValueError
        If n is negative.
    TypeError
        If n is not an integer.

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
    # ---- input validation -------------------------------------------------
    if not isinstance(n, int):
        raise TypeError("factorial is defined only for integers")
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")

    # ---- iterative computation (fast and stack‑safe) ----------------------
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Quick test run

```python
if __name__ == "__main__":
    test_vals = [0, 1, 4, 7]
    for v in test_vals:
        print(f"{v}! = {factorial(v)}")
```

**Output**

```
0! = 1
1! = 1
4! = 24
7! = 5040
```

Feel free to use the function as‑is, or adapt the error handling to suit your project's style (e.g., returning `None` instead of raising).