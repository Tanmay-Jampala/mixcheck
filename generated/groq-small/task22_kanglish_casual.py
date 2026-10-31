**Python – `merge_intervals`**

```python
from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[List[int]]:
    """
    Merge a list of [start, end] intervals.

    * Intervals that overlap **or touch** (e.g. [1, 3] and [3, 5]) are merged.
    * The result is sorted by the start value.
    * Empty input returns an empty list.

    Parameters
    ----------
    intervals : List[Tuple[int, int]]
        List of intervals where each interval is a pair (start, end).

    Returns
    -------
    List[List[int]]
        Merged, sorted list of intervals.
    """
    if not intervals:
        return []

    # 1. Sort by the start value
    intervals.sort(key=lambda x: x[0])

    merged: List[List[int]] = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        # 2. If the next interval starts before or exactly at the end
        #    of the current one, merge them.
        if start <= cur_end:          # overlap or touch
            cur_end = max(cur_end, end)
        else:
            # 3. No overlap – push the current interval and start a new one
            merged.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    # 4. Append the last interval
    merged.append([cur_start, cur_end])
    return merged
```

### Example usage

```python
intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(merge_intervals(intervals))
# Output: [[1, 6], [8, 12]]
```

The function works for any list of integer intervals, correctly handling overlapping, touching, and disjoint intervals.