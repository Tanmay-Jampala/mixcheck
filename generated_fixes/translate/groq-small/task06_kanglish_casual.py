Here’s a concise, type‑annotated implementation that does exactly what you asked for:

```python
from typing import Iterable, List

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """
    Return the sum of all even integers in *numbers*.
    If there are no even numbers, the result is 0.

    Parameters
    ----------
    numbers : Iterable[int]
        A sequence (list, tuple, generator, etc.) of integers.

    Returns
    -------
    int
        The total of all even numbers, or 0 if none exist.
    """
    # Using a generator expression keeps the memory footprint minimal
    return sum(n for n in numbers if n % 2 == 0)


# ---- Example usage ----
if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6]
    print(sum_even_numbers(sample))   # Output: 12 (2 + 4 + 6)

    empty = []
    print(sum_even_numbers(empty))    # Output: 0

    no_evens = [1, 3, 5]
    print(sum_even_numbers(no_evens)) # Output: 0
```

**Why this works**

* `sum()` on an empty generator returns `0`, so the “no even number” case is handled automatically.
* The generator expression `n for n in numbers if n % 2 == 0` iterates lazily, so it works efficiently even for large input sequences.