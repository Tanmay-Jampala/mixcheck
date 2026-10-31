Here’s a concise implementation of **`find_largest`** that follows the requirements:

```python
def find_largest(numbers):
    """
    Return the largest number in the given list.

    Parameters
    ----------
    numbers : list
        A list of numeric values (int, float, etc.).

    Returns
    -------
    The largest element in the list, or None if the list is empty.
    """
    if not numbers:          # Handles empty list (also covers None)
        return None

    # Initialize the maximum with the first element
    max_val = numbers[0]

    # Iterate through the remaining elements
    for num in numbers[1:]:
        if num > max_val:
            max_val = num

    return max_val


# Example usage
if __name__ == "__main__":
    print(find_largest([3, 1, 4, 1, 5, 9]))   # → 9
    print(find_largest([-2, -7, -1]))        # → -1
    print(find_largest([]))                  # → None
```

**Explanation**

1. **Empty‑list check** – `if not numbers:` returns `None` immediately when the list has no elements.
2. **Finding the maximum** – The function starts with the first element as the current maximum and walks through the rest of the list, updating the maximum whenever a larger value is encountered.
3. **Return** – After the loop finishes, the largest value found is returned.

Feel free to adapt the docstring or add type hints (`def find_largest(numbers: list) -> Optional[float]:`) if you need stricter typing.