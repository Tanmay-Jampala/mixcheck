```python
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping (or touching) intervals.

    Args:
        intervals: List of [start, end] intervals (inclusive).

    Returns:
        A new list of merged intervals sorted by start.
    """
    if not intervals:
        return []

    # Sort by start (and end to stabilize equal starts)
    intervals.sort(key=lambda x: (x[0], x[1]))

    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        # Overlap or touching if start <= cur_end
        if start <= cur_end:
            cur_end = max(cur_end, end)   # extend current interval
        else:
            merged.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    merged.append([cur_start, cur_end])
    return merged
```