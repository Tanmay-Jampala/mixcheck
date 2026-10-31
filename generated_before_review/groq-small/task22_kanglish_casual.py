**Python function – `merge_intervals`**

```python
def merge_intervals(intervals):
    """
    Merge a list of [start, end] intervals.

    Parameters
    ----------
    intervals : list[list[int] | tuple[int, int]]
        Each element is a 2‑item sequence where the first element is the
        start of the interval and the second element is the end.

    Returns
    -------
    list[list[int]]
        A new list of merged intervals sorted by start value.
        Intervals that *touch* (e.g. [1, 3] and [3, 5]) are treated as
        overlapping and are merged into a single interval.

    Notes
    -----
    * The input list is **not** modified.
    * Intervals are assumed to be closed: [start, end] includes both
      endpoints.
    """
    if not intervals:
        return []

    # Make a shallow copy so we don't mutate the caller's data
    sorted_ints = sorted((list(iv) for iv in intervals), key=lambda x: x[0])

    merged = [sorted_ints[0]]
    for cur_start, cur_end in sorted_ints[1:]:
        last_start, last_end = merged[-1]

        # If the current interval starts before or exactly at the end
        # of the last merged interval, they overlap/touch.
        if cur_start <= last_end:
            # Extend the last interval if needed
            merged[-1][1] = max(last_end, cur_end)
        else:
            merged.append([cur_start, cur_end])

    return merged
```

### Quick example

```python
>>> intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
>>> merge_intervals(intervals)
[[1, 6], [8, 12]]
```

The function first sorts the intervals by their start value, then iteratively merges any that overlap or touch. The result is a list of non‑overlapping, sorted intervals.