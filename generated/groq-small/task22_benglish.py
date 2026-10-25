```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : list[list[int, int]]
        List of intervals represented as [start, end].

    Returns
    -------
    list[list[int, int]]
        List of merged intervals sorted by start.
    """
    if not intervals:
        return []

    # Sort intervals by start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        # If current interval touches or overlaps the last one
        if current[0] <= last[1]:
            # Merge by extending the end if needed
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
```