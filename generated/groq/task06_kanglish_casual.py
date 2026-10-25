Here’s a concise implementation of `sum_even_numbers` in Python:

```python
def sum_even_numbers(nums):
    """
    Return the sum of all even numbers in the given list.
    If the list contains no even numbers, return 0.

    Parameters
    ----------
    nums : list[int]
        A list of integers.

    Returns
    -------
    int
        Sum of the even integers in `nums`.
    """
    # Using a generator expression to filter even numbers and sum them
    return sum(num for num in nums if num % 2 == 0)


# ---- Example usage ----
if __name__ == "__main__":
    examples = [
        [1, 2, 3, 4, 5, 6],   # → 12 (2+4+6)
        [7, 9, 11],           # → 0  (no evens)
        [],                   # → 0  (empty list)
        [0, -2, -3, 8]        # → 6  (0 + -2 + 8)
    ]

    for lst in examples:
        print(f"{lst} → {sum_even_numbers(lst)}")
```

**Explanation**

- `num % 2 == 0` checks whether a number is even.
- The generator expression `num for num in nums if num % 2 == 0` yields only the even numbers.
- `sum(...)` adds them together; if there are none, `sum` returns `0` by default, satisfying the “no even numbers” case.