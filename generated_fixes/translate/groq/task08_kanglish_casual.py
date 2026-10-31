Here’s a compact, well‑documented implementation that follows the specification:

```python
def second_largest(nums):
    """
    Return the second‑largest number in *nums*.

    Parameters
    ----------
    nums : list[Number]
        A list containing numeric values (int, float, etc.).

    Returns
    -------
    Number | None
        The second‑largest distinct value, or ``None`` if the list
        contains fewer than two distinct numbers.

    Examples
    --------
    >>> second_largest([5, 1, 9, 3])
    5
    >>> second_largest([7, 7, 7])
    None
    >>> second_largest([10])
    None
    """
    # Guard against empty / single‑element inputs early.
    if len(nums) < 2:
        return None

    # Use a set to keep only distinct values – this way duplicates of the
    # maximum don’t count as the “second” largest.
    unique_vals = set(nums)

    # If after deduplication we have fewer than two values, there is no
    # second largest.
    if len(unique_vals) < 2:
        return None

    # Remove the largest element and then take the max of what remains.
    # This is O(n) time and O(1) extra space (aside from the set).
    max_val = max(unique_vals)
    unique_vals.remove(max_val)
    return max(unique_vals)
```

### How it works
1. **Quick length check** – If the original list has fewer than two items, we can immediately return `None`.
2. **Deduplicate** – Converting to a `set` removes duplicate numbers, ensuring that the “second largest” is a *different* value from the maximum.
3. **Validate distinct count** – If the set now contains fewer than two elements, there isn’t a second distinct value, so we return `None`.
4. **Find the second largest** –  
   * Find the maximum (`max_val`).  
   * Remove it from the set.  
   * The new maximum of the reduced set is the second‑largest number.

The function runs in linear time relative to the size of the input list and uses only a modest amount of extra memory. Feel free to adapt it (e.g., to treat duplicates as valid second‑largest) by removing the `set` conversion.