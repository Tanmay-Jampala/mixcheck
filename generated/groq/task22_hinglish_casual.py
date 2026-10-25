```python
def merge_intervals(intervals):
    """
    Merge overlapping or touching intervals.

    Parameters
    ----------
    intervals : List[List[int] | Tuple[int, int]]
        A list of [start, end] pairs. `start` should be <= `end`.

    Returns
    -------
    List[List[int]]
        Merged intervals sorted by their start value.
    """
    if not intervals:
        return []

    # Sort by start (and by end to keep deterministic order)
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

    merged = [list(intervals[0])]
    for cur_start, cur_end in intervals[1:]:
        last_start, last_end = merged[-1]

        # Overlap or just touching (last_end >= cur_start)
        if last_end >= cur_start:
            merged[-1][1] = max(last_end, cur_end)   # extend the last interval
        else:
            merged.append([cur_start, cur_end])

    return merged
```