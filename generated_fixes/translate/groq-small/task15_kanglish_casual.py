Here’s a compact, efficient implementation that works for any list that contains every integer from 1 to *n* exactly once except for one missing value.  
It uses the **XOR trick** – it runs in O(n) time, O(1) extra space, and is immune to integer‑overflow problems that can arise with the arithmetic‑sum formula.

```python
def missing_number(nums):
    """
    Return the missing integer from a list that contains all numbers
    from 1 to n exactly once except for one missing value.

    Parameters
    ----------
    nums : list[int]
        List of integers containing all numbers from 1 to n except one.

    Returns
    -------
    int
        The missing number.

    Examples
    --------
    >>> missing_number([3, 1, 4, 5])
    2
    >>> missing_number([1, 2, 4, 5, 6])
    3
    """
    # XOR of all indices (1..n) and all elements in the list.
    # The missing number is the only one that appears an odd number of times.
    n = len(nums) + 1          # because one number is missing
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all
```

### Why XOR works

- XORing a number with itself cancels out (`x ^ x = 0`).
- XORing a number with 0 leaves the number unchanged (`x ^ 0 = x`).
- XOR is associative and commutative, so the order of operations doesn’t matter.

By XORing all numbers from 1 to *n* and then XORing all elements in the list, every number that appears twice (once in the full range and once in the list) cancels out, leaving only the missing number.

### Alternative: Sum formula

If you prefer the arithmetic approach, you can also do:

```python
def missing_number_sum(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)
```

Both functions give the same result; choose the one that best fits your style or constraints.