```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : list[list[int]]
        A list of [start, end] pairs.  Intervals are assumed to be
        inclusive on both ends.  Intervals may be unsorted and may
        even have start > end – in that case the pair is swapped.

    Returns
    -------
    list[list[int]]
        A new list of merged intervals sorted by start.

    Notes
    -----
    Two intervals are considered overlapping if they share at least one
    point, i.e. if the start of the second interval is less than or
    equal to the end of the first interval.  This also treats
    "touching" intervals (e.g. [1, 3] and [3, 5]) as overlapping.

    Complexity
    ----------
    O(n log n) time due to sorting, O(n) additional space.
    """
    if not intervals:
        return []

    # Normalise intervals so that start <= end
    norm = []
    for s, e in intervals:
        if s > e:
            s, e = e, s
        norm.append([s, e])

    # Sort by start
    norm.sort(key=lambda x: x[0])

    merged = [norm[0]]
    for cur_start, cur_end in norm[1:]:
        last_start, last_end = merged[-1]
        # Overlap or touch if cur_start <= last_end
        if cur_start <= last_end:
            # Extend the last interval
            merged[-1][1] = max(last_end, cur_end)
        else:
            merged.append([cur_start, cur_end])

    return merged
```

### Example

```python
>>> intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
>>> merge_intervals(intervals)
[[1, 6], [8, 12]]
```

The function works for unsorted input, handles touching intervals, and returns a sorted list of merged intervals.