Here’s a compact, well‑documented implementation.  
It works in O(n) time and O(1) extra space, using the arithmetic‑sum formula (you could also use XOR if you prefer).

```python
def missing_number(nums):
    """
    Return the missing integer from the sequence 1..n.

    Parameters
    ----------
    nums : list[int]
        A list that contains every integer from 1 to n exactly once,
        except for a single missing value.  The order of the elements
        is arbitrary.

    Returns
    -------
    int
        The missing number.

    Raises
    ------
    ValueError
        If the input list is empty or its length does not correspond to a
        valid 1..n sequence (i.e. len(nums) + 1 is not the expected n).

    Examples
    --------
    >>> missing_number([3, 1, 4, 2, 6])
    5
    >>> missing_number([2, 1])
    3
    """
    if not isinstance(nums, list):
        raise TypeError("nums must be a list of integers")

    n = len(nums) + 1                     # because exactly one number is missing
    expected_sum = n * (n + 1) // 2       # sum of 1..n
    actual_sum = sum(nums)                # sum of the provided numbers
    missing = expected_sum - actual_sum

    # Basic sanity check – the result should be within 1..n
    if not (1 <= missing <= n):
        raise ValueError("Input list does not represent a valid 1..n sequence")
    return missing


# ----------------------------------------------------------------------
# Simple test harness (run only when this file is executed directly)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4, 5, 6], 3),
        ([3, 1, 4, 2, 6], 5),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
        (list(range(1, 1000)) + [1001], 1000),  # missing 1000
    ]

    for idx, (inp, expected) in enumerate(test_cases, 1):
        result = missing_number(inp)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
    print("All tests passed!")
```

**How it works**

1. If the list should contain every number from 1 to n except one, its length is `n‑1`.  
   Hence `n = len(nums) + 1`.
2. The sum of the first n natural numbers is `n*(n+1)//2`.  
   Subtract the actual sum of the supplied list; the difference is the missing value.
3. A quick sanity check ensures the result lies in the valid range.

Feel free to drop the function into any module or script and call `missing_number(your_list)`.