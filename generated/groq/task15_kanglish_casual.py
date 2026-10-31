**Python function – `missing_number`**

```python
def missing_number(arr):
    """
    1‑ರಿಂದ n ವರೆಗೆ (ಒಂದು ಸಂಖ್ಯೆ ಹೊರತುಪಡಿಸಿ) ಇರುವ ಎಲ್ಲಾ ಪೂರ್ಣಾಂಕಗಳ
    ಪಟ್ಟಿಯನ್ನು (order ಯಾವುದು ಆಗಿರಲಿ) ನೀಡಿದಾಗ, ಕಳೆದುಹೋದ ಸಂಖ್ಯೆಯನ್ನು
    ಹಿಂತಿರುಗಿಸುವ ಫಂಕ್ಷನ್.

    Parameters
    ----------
    arr : list[int]
        1‑ರಿಂದ n ವರೆಗೆ ಇರುವ ಸಂಖ್ಯೆಗಳು, ಒಂದನ್ನು ಹೊರತುಪಡಿಸಿ, ಯಾವುದೇ ಕ್ರಮದಲ್ಲಿ.

    Returns
    -------
    int
        ಕಳೆದುಹೋದ ಸಂಖ್ಯೆ.  (arr ಖಾಲಿ ಇದ್ದರೆ 0 ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.)

    ಉದಾಹರಣೆ
    -------
    >>> missing_number([3, 1, 4, 2, 6])
    5
    >>> missing_number([2, 3, 1, 5])
    4
    """
    if not arr:                     # ಖಾಲಿ ಪಟ್ಟಿಗೆ ವಿಶೇಷ ನಿರ್ವಹಣೆ
        return 0

    n = len(arr) + 1                # ಏಕೆಂದರೆ ಒಂದು ಸಂಖ್ಯೆ ಕಳೆದುಹೋಗಿದೆ
    # 1‑ರಿಂದ n ವರೆಗೆ ಇರುವ ಮೊತ್ತದ ಸೂತ್ರ: n*(n+1)//2
    expected_sum = n * (n + 1) // 2
    actual_sum   = sum(arr)

    return expected_sum - actual_sum
```

### ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?

1. **`n` ಅನ್ನು ನಿರ್ಧರಿಸುವುದು**  
   ಪಟ್ಟಿಯಲ್ಲಿ `len(arr)` ಸಂಖ್ಯೆಗಳು ಇವೆ, ಆದರೆ 1‑ರಿಂದ `n` ವರೆಗೆ `n` ಸಂಖ್ಯೆಗಳು ಇರಬೇಕಾಗಿರುವುದರಿಂದ  
   `n = len(arr) + 1`.

2. **ಅಪೇಕ್ಷಿತ ಮೊತ್ತ**  
   1‑ರಿಂದ `n` ವರೆಗೆ ಇರುವ ಎಲ್ಲಾ ಸಂಖ್ಯೆಗಳ ಮೊತ್ತ = `n*(n+1)//2`.

3. **ವಾಸ್ತವಿಕ ಮೊತ್ತ**  
   `sum(arr)` – ಪಟ್ಟಿಯಲ್ಲಿ ಇರುವ ಸಂಖ್ಯೆಗಳ ಮೊತ್ತ.

4. **ಕಳೆದುಹೋದ ಸಂಖ್ಯೆ**  
   `expected_sum - actual_sum` → ಕಳೆದುಹೋದ ಸಂಖ್ಯೆ.

### ಇನ್ನೊಂದು ಆಯ್ಕೆ – XOR (O(1) ಹೆಚ್ಚುವರಿ ಮೆಮೊರಿ)

```python
def missing_number_xor(arr):
    """XOR ಬಳಸಿ ಕಳೆದುಹೋದ ಸಂಖ್ಯೆಯನ್ನು ಕಂಡುಹಿಡಿಯುವ ಆವೃತ್ತಿ."""
    if not arr:
        return 0

    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    # 1‑ರಿಂದ n ವರೆಗೆ XOR
    for i in range(1, n + 1):
        xor_all ^= i

    # ಪಟ್ಟಿಯಲ್ಲಿನ XOR
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr
```

### ಪರೀಕ್ಷೆ (ಉದಾಹರಣೆ)

```python
if __name__ == "__main__":
    tests = [
        ([1, 2, 4, 5], 3),
        ([5, 3, 2, 1], 4),
        ([2, 3, 1, 5, 6, 7, 8, 9, 10], 4),
        ([1], 2),               # n = 2, 2 ಕಳೆದುಹೋಗಿದೆ
        ([], 0),                # ಖಾಲಿ ಪಟ್ಟಿಗೆ 0 ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ
    ]

    for lst, expected in tests:
        got = missing_number(lst)
        assert got == expected, f"Failed for {lst}: got {got}, expected {expected}"
    print("All tests passed!")
```

ಈ ಫಂಕ್ಷನ್‌ಗಳು **O(n)** ಸಮಯ ಮತ್ತು **O(1)** ಹೆಚ್ಚುವರಿ ಮೆಮೊರಿಯಲ್ಲಿ (ಸೂತ್ರ‑ಆಧಾರಿತ) ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಆದ್ದರಿಂದ ದೊಡ್ಡ ಪಟ್ಟಿಗಳಿಗೂ ಪರಿಣಾಮಕಾರಿಯಾಗಿದೆ.