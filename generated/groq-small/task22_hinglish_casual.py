```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : list of [start, end]
        List of intervals. Intervals may be unsorted.

    Returns
    -------
    list of [start, end]
        Sorted list of merged intervals.
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        # If the next interval starts before or exactly at the end of the current one,
        # merge them (touching intervals are considered overlapping).
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            merged.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    # Append the last interval
    merged.append([cur_start, cur_end])
    return merged
```