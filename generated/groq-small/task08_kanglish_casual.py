**Python – `second_largest` ಫಂಕ್ಷನ್**

```python
from __future__ import annotations
from typing import List, Optional

def second_largest(nums: List[int]) -> Optional[int]:
    """
    Return the second‑largest value in a list of distinct integers.

    Parameters
    ----------
    nums : List[int]
        List of integers. All values are guaranteed to be different.

    Returns
    -------
    Optional[int]
        The second‑largest integer if the list contains at least two
        elements; otherwise `None`.

    Examples
    --------
    >>> second_largest([5, 1, 9, 3])
    5
    >>> second_largest([42])
    None
    >>> second_largest([])
    None
    """
    # Not enough elements → no second largest
    if len(nums) < 2:
        return None

    # Keep track of the largest and second largest seen so far
    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second:
            second = n

    return second
```

### Why this works

* The list is guaranteed to contain **distinct** numbers, so we don't have to worry about ties.
* We iterate once over the list (`O(n)` time) and keep only two variables (`first` and `second`), so the memory usage is `O(1)`.
* If the list has fewer than two elements we immediately return `None`, satisfying the requirement.

Feel free to drop this function into your project or adapt it to other numeric types (e.g., `float`, `int`, `Decimal`) by changing the type hints.