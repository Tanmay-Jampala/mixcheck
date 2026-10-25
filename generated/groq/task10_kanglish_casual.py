**Python‑ನಲ್ಲಿ Fibonacci ಫಂಕ್ಷನ್**

```python
def fibonacci(n: int) -> int:
    """
    n‑ನೇ Fibonacci ಸಂಖ್ಯೆಯನ್ನು ಹಿಂತಿರುಗಿಸುವುದು.
    ನಿರ್ವಚನೆ:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(k) = fibonacci(k‑1) + fibonacci(k‑2)   (k ≥ 2)

    Parameters
    ----------
    n : int
        ಹುಡುಕಬೇಕಾದ ಸ್ಥಾನ (0‑ಆಧಾರಿತ).

    Returns
    -------
    int
        n‑ನೇ Fibonacci ಸಂಖ್ಯೆ.

    Raises
    ------
    ValueError
        n ನೆಗೆಟಿವ್ ಆಗಿದ್ದರೆ.
    """
    if n < 0:
        raise ValueError("n must be a non‑negative integer")

    # ಮೂಲ ಪ್ರಕರಣಗಳು
    if n == 0:
        return 0
    if n == 1:
        return 1

    # ಇಟರೇಟಿವ್ (O(n) ಸಮಯ, O(1) ಸ್ಥಳ) ಅನುಷ್ಠಾನ
    a, b = 0, 1          # a = fibonacci(i‑2), b = fibonacci(i‑1)
    for _ in range(2, n + 1):
        a, b = b, a + b   # ಹೊಸ fibonacci(i) = a + b
    return b
```

### ಹೇಗೆ ಬಳಸುವುದು

```python
if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
```

**ಫಲಿತಾಂಶ**

```
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
```

### ಟಿಪ್ಪಣಿಗಳು

* ಈ ಅನುಷ್ಠಾನವು **ಇಟರೇಟಿವ್** ಆಗಿದೆ, ಆದ್ದರಿಂದ ಪುನರಾವರ್ತನೆ (recursion) ಬಳಸುವ exponential‑time ಪರಿಹಾರಕ್ಕಿಂತ ಬಹಳ ವೇಗವಾಗಿರುತ್ತದೆ.  
* ಸಮಯ ಸಂಕೀರ್ಣತೆ **O(n)**, ಹೆಚ್ಚುವರಿ ಮೆಮೊರಿ **O(1)**.  
* `n` ನೆಗೆಟಿವ್ ಆಗಿದ್ದರೆ `ValueError` ಎಸೆದು, ತಪ್ಪು ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಸೂಚಿಸುತ್ತದೆ.  

ಇದು ನಿಮಗೆ ಬೇಕಾದ “nth Fibonacci number” ಅನ್ನು ನೀಡುವ ಸರಳ ಹಾಗೂ ಪರಿಣಾಮಕಾರಿ ಫಂಕ್ಷನ್. 🎉