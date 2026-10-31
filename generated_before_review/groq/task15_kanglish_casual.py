**Solution Overview**

We need a function `missing_number(nums, n)` that receives  

* `nums` – a list that contains **all** integers from `1` to `n` **except one** (the order can be arbitrary).  
* `n` – the upper bound of the expected range.

The function must return the missing integer.

The classic way is to use the arithmetic series formula  

\[
\text{sum}_{1..n}= \frac{n\,(n+1)}{2}
\]

and subtract the sum of the given list.  
The difference is the missing number.

We’ll also add a tiny safety‑check: if the list length isn’t `n‑1` or if the computed result is out of range, we raise a `ValueError`. This makes the function easier to debug when it’s used incorrectly.

---

## Code

```python
def missing_number(nums, n):
    """
    Return the missing integer from the sequence 1..n.

    Parameters
    ----------
    nums : list[int]
        List containing all numbers from 1 to n except one.
        Order does not matter.
    n : int
        The upper bound of the expected range (inclusive).

    Returns
    -------
    int
        The missing number.

    Raises
    ------
    ValueError
        If the input list length is not n-1 or the computed missing
        number is not in the range 1..n.
    """
    # Basic validation
    if len(nums) != n - 1:
        raise ValueError(
            f"Expected list length {n-1} (one missing), got {len(nums)}."
        )

    # Expected sum of 1..n
    expected_sum = n * (n + 1) // 2
    # Actual sum of the provided numbers
    actual_sum = sum(nums)

    missing = expected_sum - actual_sum

    # Final sanity check
    if not (1 <= missing <= n):
        raise ValueError(f"Computed missing number {missing} is out of range 1..{n}.")

    return missing
```

---

## How It Works (Step‑by‑Step)

| Step | What Happens | Why It Works |
|------|--------------|--------------|
| 1️⃣   | Compute `expected_sum = n*(n+1)//2` | This is the sum of the complete series `1,2,…,n`. |
| 2️⃣   | Compute `actual_sum = sum(nums)` | Adds up the numbers we actually have. |
| 3️⃣   | `missing = expected_sum - actual_sum` | The only number not present is exactly the difference. |
| 4️⃣   | Return `missing` | Gives the answer. |

The algorithm runs in **O(n)** time (the `sum` traverses the list once) and uses **O(1)** extra space.

---

## Quick Test Suite

```python
def _run_tests():
    test_cases = [
        # (input list, n, expected missing)
        ([1, 2, 4, 5], 5, 3),
        ([5, 3, 2, 1], 5, 4),
        (list(range(2, 101)), 100, 1),          # missing 1
        (list(range(1, 100)), 100, 100),        # missing 100
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1),  # missing 1, unsorted
    ]

    for i, (lst, n, expected) in enumerate(test_cases, 1):
        result = missing_number(lst, n)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
        print(f"✅ Test {i} passed (missing = {result})")

if __name__ == "__main__":
    _run_tests()
```

Running the script prints:

```
✅ Test 1 passed (missing = 3)
✅ Test 2 passed (missing = 4)
✅ Test 3 passed (missing = 1)
✅ Test 4 passed (missing = 100)
✅ Test 5 passed (missing = 1)
```

---

### Alternative (XOR) Approach

If you prefer a solution that never overflows (useful for extremely large `n`), you can use the XOR trick:

```python
def missing_number_xor(nums, n):
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    xor_given = 0
    for x in nums:
        xor_given ^= x

    return xor_all ^ xor_given
```

Both versions have the same `O(n)` time and `O(1)` space characteristics; the arithmetic‑sum version is usually a bit clearer.

---

**Enjoy coding!** 🚀 If you have any extra requirements (e.g., handling duplicates, returning all missing numbers, etc.) just let me know.