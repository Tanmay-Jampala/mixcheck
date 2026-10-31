Sure! Below is a clean, efficient Python implementation that returns the **n‑th Fibonacci number** with the standard base cases

```
fibonacci(0) = 0
fibonacci(1) = 1
```

I’ll give you two versions:

1. **Iterative (O(n) time, O(1) space)** – best for large `n`.
2. **Recursive with memoization (O(n) time, O(n) space)** – nice for learning.

---

## 1️⃣ Iterative version (recommended)

```python
def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number.
    Uses an iterative approach – O(n) time, O(1) space.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1          # F(0), F(1)
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

### Usage

```python
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(10))  # 55
print(fibonacci(50))  # 12586269025
```

---

## 2️⃣ Recursive with memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_rec(n: int) -> int:
    """
    Recursive Fibonacci with memoization.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
```

This version is great for teaching recursion, but the iterative one is usually faster for very large `n`.

---

### Quick sanity check

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

---

### Bonus: Big‑integer support

Python’s `int` type automatically handles arbitrarily large integers, so you can safely compute `fibonacci(1000)` or even `fibonacci(10000)` with the iterative version.

```python
print(fibonacci(1000))  # 434665576869374564356885276750406258025646605173717804024817290895... (a 209‑digit number)
```

Happy coding! If you need any tweaks (e.g., modulo arithmetic, matrix exponentiation, etc.), just let me know.