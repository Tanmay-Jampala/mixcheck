Here’s a compact, efficient implementation that follows the classic definition:

```python
def fibonacci(n: int) -> int:
    """
    Return the n‑th Fibonacci number (0‑based indexing).

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to compute.
        Must be a non‑negative integer.

    Returns
    -------
    int
        The n‑th Fibonacci number.

    Examples
    --------
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Iterative approach – O(n) time, O(1) space
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Why this version?

* **Iterative** – avoids the exponential blow‑up of naive recursion.
* **O(1) space** – only two integer variables are kept.
* **Clear base cases** – `fibonacci(0)` and `fibonacci(1)` are handled explicitly.
* **Type hints & docstring** – makes the function self‑documenting and easy to use in larger projects.

Feel free to drop this into your module or adapt it for memoization if you need to compute many Fibonacci numbers in a single run.