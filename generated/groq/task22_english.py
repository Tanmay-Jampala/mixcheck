```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Args:
        intervals (list[list[int]]): List of [start, end] intervals.

    Returns:
        list[list[int]]: Merged intervals sorted by start.
    """
    if not intervals:
        return []

    # Sort by start (and by end to stabilize equal starts)
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

    merged = [intervals[0][:]]  # copy first interval
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        # Overlap or touch if current start <= last_end
        if start <= last_end:
            merged[-1][1] = max(last_end, end)  # extend the last interval
        else:
            merged.append([start, end])

    return merged
```