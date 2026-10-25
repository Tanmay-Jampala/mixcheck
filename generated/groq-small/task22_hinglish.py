```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : list[list[int]]
        List of [start, end] intervals.

    Returns
    -------
    list[list[int]]
        Merged intervals sorted by start.
    """
    if not intervals:
        return []

    # Sort by start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        # If current starts before or at the end of last (touching counts)
        if current[0] <= last[1]:
            # Merge by extending the end if needed
            last[1] = max(last[1], current[1])
        else:
            merged.append(current[:])  # copy to avoid mutation

    return merged
```