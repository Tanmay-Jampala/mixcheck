Sure!  
Here’s a simple, clean Python function that returns the largest number in a list, or `None` if the list is empty.

```python
from typing import List, Optional, Union

def find_largest(numbers: List[Union[int, float]]) -> Optional[Union[int, float]]:
    """
    Return the largest number in `numbers`.
    
    Parameters
    ----------
    numbers : list of int or float
        The list to search.

    Returns
    -------
    int | float | None
        The maximum value, or None if the list is empty.
    """
    if not numbers:          # Empty list check
        return None
    return max(numbers)      # Built‑in max handles the rest
```

### Usage examples

```python
print(find_largest([3, 7, 2, 9]))   # → 9
print(find_largest([-5, -2, -10]))  # → -2
print(find_largest([]))             # → None
```

The function uses Python’s built‑in `max()` for efficiency, and the `if not numbers` guard ensures we return `None` for an empty list. Feel free to drop it into your project!