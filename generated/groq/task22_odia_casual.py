```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping or touching intervals.

    Args:
        intervals: List of [start, end] pairs.

    Returns:
        A new list of merged intervals sorted by start.
    """
    if not intervals:
        return []

    # Sort by the start of each interval
    intervals = sorted(intervals, key=lambda x: x[0])

    merged = [intervals[0][:]]  # make a copy to avoid mutating input
    for cur_start, cur_end in intervals[1:]:
        prev_start, prev_end = merged[-1]

        # Overlap or just touching (prev_end >= cur_start)
        if cur_start <= prev_end:
            merged[-1][1] = max(prev_end, cur_end)
        else:
            merged.append([cur_start, cur_end])

    return merged
```