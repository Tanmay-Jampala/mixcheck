```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : list of [start, end]
        List of intervals where start <= end.

    Returns
    -------
    list of [start, end]
        Sorted and merged intervals.
    """
    if not intervals:
        return []

    # Sort by start value
    intervals = sorted(intervals, key=lambda x: x[0])

    merged = [intervals[0][:]]  # make a copy of the first interval
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # overlap or touch
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```