Sure!  
Here’s a clean, efficient Python function that returns the **n‑th Fibonacci number** with the standard base cases

```
fibonacci(0) = 0
fibonacci(1) = 1
```

I’ll give you a few versions so you can pick the one that best fits your needs.

---

## 1️⃣ Iterative (fast & memory‑friendly)

```python
def fibonacci(n: int) -> int:
    """Return the n‑th Fibonacci number (0‑based)."""
    if n < 0:
        raise ValueError("n must be a non‑negative integer")

    a, b = 0, 1          # f(0), f(1)
    for _ in range(n):
        a, b = b, a + b  # shift forward
    return a
```

* **Time complexity:** `O(n)`  
* **Space complexity:** `O(1)`  

---

## 2️⃣ Recursive (simple but not efficient for large n)

```python
def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

* **Time complexity:** `O(2^n)` – exponential, so use only for small `n`.  
* **Space complexity:** `O(n)` due to recursion depth.

---

## 3️⃣ Recursive with memoization (fast for many calls)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
```

* **Time complexity:** `O(n)` after the first call.  
* **Space complexity:** `O(n)` for the cache.

---

## 4️⃣ Using Binet’s formula (closed‑form, but beware of floating‑point errors)

```python
import math

def fibonacci_binet(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non‑negative integer")
    phi = (1 + math.sqrt(5)) / 2
    return round(phi**n / math.sqrt(5))
```

* Works well for `n` up to about 70–75 before floating‑point rounding errors creep in.

---

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

---

### Which one to use?

| Scenario | Recommended |
|----------|-------------|
| Small `n` (≤ 30) | Any version |
| Large `n` (≤ 10⁶) | Iterative or memoized |
| Many repeated calls | Memoized |
| Need a single formula | Binet (but watch precision) |

Feel free to copy the snippet that best matches your use case. Happy coding!