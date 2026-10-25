```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : List[List[int]]
        List of intervals where each interval is [start, end].

    Returns
    -------
    List[List[int]]
        Merged intervals sorted by start.
    """
    if not intervals:
        return []

    # Sort by start (and by end to stabilize equal starts)
    intervals.sort(key=lambda x: (x[0], x[1]))

    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        # Overlap or touch if start <= cur_end
        if start <= cur_end:
            cur_end = max(cur_end, end)   # extend current interval
        else:
            merged.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    merged.append([cur_start, cur_end])
    return merged
```