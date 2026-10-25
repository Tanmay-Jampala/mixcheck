```python
def merge_intervals(intervals):
    """
    Merge overlapping (or touching) intervals.

    Parameters
    ----------
    intervals : List[List[int]]
        A list of intervals, each represented as [start, end].

    Returns
    -------
    List[List[int]]
        A new list of merged intervals, sorted by start.
    """
    if not intervals:
        return []

    # Sort intervals by their start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0][:]]  # make a copy of the first interval
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        # If the current interval overlaps or touches the last merged one,
        # extend the last merged interval.
        if start <= last_end:          # overlap or touch
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```