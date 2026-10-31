Here’s a simple, self‑contained implementation of a `fibonacci` function in Python. It handles the base cases `fibonacci(0) = 0` and `fibonacci(1) = 1` and works efficiently for moderately large `n` by using an iterative approach (O(n) time, O(1) space).

```python
def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to compute.
        Must be a non‑negative integer (n >= 0).

    Returns
    -------
    int
        The nth Fibonacci number, where:
        - fibonacci(0) == 0
        - fibonacci(1) == 1
        - fibonacci(n) == fibonacci(n-1) + fibonacci(n-2) for n >= 2

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")

    # Handle the two trivial base cases directly
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Iterative computation: keep only the two most recent values
    prev, cur = 0, 1   # prev = F(0), cur = F(1)
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur   # cur becomes F(i), prev becomes F(i‑1)

    return cur


# Example usage:
if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
```

**Explanation of the algorithm**

1. **Input validation** – The function checks that `n` is non‑negative and raises a clear error otherwise.
2. **Base cases** – For `n = 0` and `n = 1` the function returns the known values immediately.
3. **Iterative loop** – Starting from `i = 2`, it repeatedly updates two variables:
   * `prev` holds `F(i‑1)`
   * `cur` holds `F(i)`
   This avoids the exponential blow‑up of the naïve recursive version and uses only constant extra memory.

Feel free to adapt the function (e.g., add memoization or use matrix exponentiation) if you need to compute very large Fibonacci numbers more quickly.