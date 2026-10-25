Sure!  
Here’s a compact, ready‑to‑use Python function that sums all the even numbers in a list of integers.  
If the list contains no even numbers, it simply returns `0`.

```python
def sum_even_numbers(nums: list[int]) -> int:
    """
    Return the sum of all even integers in `nums`.

    Parameters
    ----------
    nums : list[int]
        A list of integers.

    Returns
    -------
    int
        Sum of the even numbers.  If there are no even numbers, returns 0.
    """
    # The generator expression yields only even numbers.
    # `sum()` of an empty generator is 0, so no extra check is needed.
    return sum(n for n in nums if n % 2 == 0)


# ---- Example usage ----
if __name__ == "__main__":
    sample = [1, 4, 7, 10, 13]
    print(sum_even_numbers(sample))   # Output: 14  (4 + 10)

    empty_even = [1, 3, 5]
    print(sum_even_numbers(empty_even))  # Output: 0
```

### Why this works
- `n % 2 == 0` is `True` only for even numbers.
- The generator expression `n for n in nums if n % 2 == 0` yields just those evens.
- `sum()` adds them up; if the generator is empty, `sum()` returns `0` automatically.

Feel free to drop this function into your project or tweak it (e.g., add type hints, logging, etc.) as needed!