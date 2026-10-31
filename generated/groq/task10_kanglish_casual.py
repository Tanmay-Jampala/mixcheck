Here’s a clean, Python‑ic implementation of a function that returns the *n*‑th Fibonacci number with the required base cases  

```python
def fibonacci(n: int) -> int:
    """
    Return the n‑th Fibonacci number.
    
    Definitions:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n‑1) + fibonacci(n‑2)   for n >= 2
    
    Parameters
    ----------
    n : int
        The index (must be a non‑negative integer).

    Returns
    -------
    int
        The n‑th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")

    # Fast path for the two base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Iterative DP – O(n) time, O(1) extra space
    a, b = 0, 1          # a = F(i‑2), b = F(i‑1)
    for _ in range(2, n + 1):
        a, b = b, a + b  # now b = F(i)
    return b
```

### How it works
1. **Input validation** – we raise an error for negative indices because the classic Fibonacci sequence is defined only for `n >= 0`.
2. **Base cases** – `0` and `1` are returned directly.
3. **Iterative loop** – we keep only the two most recent Fibonacci numbers (`a` and `b`).  
   Each iteration updates them so that `b` becomes the next Fibonacci number.  
   This runs in linear time `O(n)` and uses constant extra memory `O(1)`.

### Quick test

```python
for i in range(10):
    print(i, fibonacci(i))
```

Output:

```
0 0
1 1
2 1
3 2
4 3
5 5
6 8
7 13
8 21
9 34
```

Feel free to copy the function into your project. If you need a version that works for very large `n` (e.g., using matrix exponentiation or fast doubling) just let me know!