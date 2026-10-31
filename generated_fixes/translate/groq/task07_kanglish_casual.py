Here’s a clean, well‑documented implementation of a `factorial` function that follows the usual mathematical definition:

```python
def factorial(n: int) -> int:
    """
    Compute the factorial of a non‑negative integer.

    Parameters
    ----------
    n : int
        The number whose factorial is required.  Must be >= 0.

    Returns
    -------
    int
        n! (the product of all positive integers ≤ n).  By definition,
        factorial(0) == 1.

    Raises
    ------
    ValueError
        If ``n`` is negative.
    TypeError
        If ``n`` is not an integer.

    Examples
    --------
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(-3)
    Traceback (most recent call last):
        ...
    ValueError: factorial is not defined for negative numbers
    """
    # ---- Input validation -------------------------------------------------
    if not isinstance(n, int):
        raise TypeError(f"factorial() only accepts integer arguments, got {type(n).__name__}")

    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")

    # ---- Base case ---------------------------------------------------------
    if n == 0:
        return 1

    # ---- Iterative computation (avoids recursion depth limits) ------------
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### How it works
1. **Validation** – The function first checks that the argument is an integer and that it isn’t negative.  
2. **Base case** – By definition, `0!` equals `1`.  
3. **Computation** – It then multiplies the numbers `2 … n` together in a simple loop.  
   *Using an iterative loop instead of recursion prevents hitting Python’s recursion depth limit for large `n`.*

### Quick test

```python
if __name__ == "__main__":
    test_values = [0, 1, 4, 5, 10]
    for v in test_values:
        print(f"{v}! = {factorial(v)}")
```

Output:

```
0! = 1
1! = 1
4! = 24
5! = 120
10! = 3628800
```

Feel free to drop the function into any module or script where you need factorials!