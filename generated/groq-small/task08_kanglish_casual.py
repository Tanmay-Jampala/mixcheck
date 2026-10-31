**Python – `second_largest` ಫಂಕ್ಷನ್**

```python
from typing import List, Optional

def second_largest(nums: List[int]) -> Optional[int]:
    """
    Return the second largest element in a list of distinct integers.
    If the list contains fewer than 2 elements, return None.

    Parameters
    ----------
    nums : List[int]
        List of distinct integers.

    Returns
    -------
    Optional[int]
        The second largest integer, or None if not enough elements.
    """
    # Quick check – we need at least two numbers
    if len(nums) < 2:
        return None

    # Initialise the two largest values
    # Use the first two elements to start
    first, second = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])

    # Iterate over the rest of the list
    for n in nums[2:]:
        if n > first:
            second = first
            first = n
        elif n > second:
            second = n

    return second
```

### How it works

1. **Length check** – If the list has fewer than two elements we immediately return `None`.
2. **Initialisation** – We set `first` and `second` to the larger and smaller of the first two numbers.
3. **Single pass** – For every remaining element:
   * If it’s larger than the current `first`, the old `first` becomes the new `second`, and the element becomes the new `first`.
   * Otherwise, if it’s larger than the current `second`, it becomes the new `second`.
4. After the loop, `second` holds the second‑largest value.

### Example usage

```python
print(second_largest([5, 1, 9, 3, 7]))   # → 7
print(second_largest([42, 17]))          # → 17
print(second_largest([10]))              # → None
print(second_largest([]))                # → None
```

### Alternative (simpler but less efficient)

If you don’t mind the extra memory and want a one‑liner:

```python
def second_largest_simple(nums: List[int]) -> Optional[int]:
    return sorted(nums, reverse=True)[1] if len(nums) >= 2 else None
```

This sorts the list (O(n log n)) and picks the second element. The first implementation is O(n) time and O(1) extra space.