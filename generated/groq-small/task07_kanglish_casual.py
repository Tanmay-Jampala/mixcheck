**Python – Factorial Function (no negative inputs, 0 ! = 1)**  

```python
def factorial(n: int) -> int:
    """
    Return the factorial of a non‑negative integer `n`.

    Parameters
    ----------
    n : int
        The number to compute the factorial of. Must be >= 0.

    Returns
    -------
    int
        n!  (1 for n == 0)

    Raises
    ------
    ValueError
        If `n` is negative.
    TypeError
        If `n` is not an integer.

    Examples
    --------
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(-3)
    Traceback (most recent call last):
        ...
    ValueError: factorial is not defined for negative numbers
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError(f"factorial() only accepts integers, got {type(n).__name__}")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")

    # Iterative implementation (fast and safe for large n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Why this implementation?

| Feature | Why it matters |
|---------|----------------|
| **Input type check** | Prevents accidental passing of floats, strings, etc. |
| **Negative‑check** | Meets the requirement “n negative irolla” (do not allow negative). |
| **Iterative loop** | Avoids recursion depth limits and is more memory‑efficient than recursion. |
| **Docstring** | Gives clear usage, examples, and error information. |

---

#### Quick test

```python
if __name__ == "__main__":
    for x in range(6):
        print(f"{x}! = {factorial(x)}")
```

Output:

```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

Feel free to copy‑paste the function into your project!