Here’s a compact, type‑annotated implementation that runs in **O(n)** time and **O(1)** extra space:

```python
from typing import List, Optional, Union

Number = Union[int, float]   # adjust if you only want ints

def second_largest(nums: List[Number]) -> Optional[Number]:
    """
    Return the second largest distinct number in *nums*.
    If the list contains fewer than two elements, return None.

    Parameters
    ----------
    nums : list[Number]
        A list of distinct numbers (int or float).

    Returns
    -------
    Number | None
        The second largest number, or None if not enough elements.
    """
    if len(nums) < 2:
        return None

    # Initialise the two largest values
    first = second = None

    for n in nums:
        if first is None or n > first:
            second = first
            first = n
        elif second is None or n > second:
            second = n

    return second
```

### How it works

1. **Early exit** – If the list has fewer than two elements we immediately return `None`.
2. **Single pass** – We keep track of the largest (`first`) and second largest (`second`) values seen so far.
3. **Update logic**  
   * If the current number `n` is larger than `first`, the old `first` becomes the new `second`, and `n` becomes the new `first`.  
   * Otherwise, if `n` is larger than `second`, we update `second` only.
4. Because the input list contains distinct numbers, we don’t need to handle equality cases.

### Example usage

```python
print(second_largest([3, 1, 4, 2]))   # → 3
print(second_largest([10, 20]))       # → 10
print(second_largest([5]))            # → None
print(second_largest([]))             # → None
```

Feel free to adjust the `Number` type alias if you want to restrict the function to integers only.