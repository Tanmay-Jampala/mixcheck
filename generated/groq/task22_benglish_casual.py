```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : List[Tuple[int, int]] or List[List[int]]
        A list of [start, end] intervals.

    Returns
    -------
    List[List[int]]
        Sorted list of merged intervals.
    """
    if not intervals:
        return []

    # Ensure we work with mutable lists
    intervals = [list(iv) for iv in intervals]

    # Sort by start (and by end to keep deterministic order)
    intervals.sort(key=lambda x: (x[0], x[1]))

    merged = [intervals[0]]
    for cur_start, cur_end in intervals[1:]:
        last_start, last_end = merged[-1]

        # Overlap or just touching (last_end >= cur_start)
        if last_end >= cur_start:
            merged[-1][1] = max(last_end, cur_end)   # extend the last interval
        else:
            merged.append([cur_start, cur_end])

    return merged
```