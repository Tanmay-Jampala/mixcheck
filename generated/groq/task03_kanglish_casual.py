Here’s a simple, well‑documented implementation of **`find_largest`** that follows the requirements:

```python
from typing import List, Optional, Union

Number = Union[int, float]          # you can extend this if you need other numeric types


def find_largest(numbers: List[Number]) -> Optional[Number]:
    """
    Return the largest element in *numbers*.

    Parameters
    ----------
    numbers : List[Number]
        A list containing numeric values (int, float, …).

    Returns
    -------
    Optional[Number]
        The maximum value in the list, or ``None`` if the list is empty.

    Examples
    --------
    >>> find_largest([3, 1, 4, 2])
    4
    >>> find_largest([])
    None
    """
    if not numbers:          # empty list → return None
        return None

    # Initialise the maximum with the first element and scan the rest.
    max_val = numbers[0]
    for n in numbers[1:]:
        if n > max_val:
            max_val = n
    return max_val


# ----------------------------------------------------------------------
# Quick demo (you can delete or comment this part in production code)
if __name__ == "__main__":
    print(find_largest([10, -5, 3.2, 7]))   # → 10
    print(find_largest([]))                # → None
```

### How it works
1. **Empty‑list check** – `if not numbers:` catches `[]` (or any falsy iterable) and returns `None` immediately.
2. **Linear scan** – Starting with the first element as the provisional maximum, we iterate through the rest of the list, updating `max_val` whenever we see a larger value.  
   This runs in **O(n)** time and uses **O(1)** extra space.
3. **Type hints** – `List[Number]` and `Optional[Number]` make the expected input and output clear to readers and static analysis tools.

Feel free to adapt the function (e.g., raise an exception for an empty list, support custom comparison keys, etc.) based on your project’s needs.