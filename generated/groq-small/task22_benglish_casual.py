```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for cur in intervals[1:]:
        last = merged[-1]
        # Merge if intervals overlap or touch (end == next start)
        if cur[0] <= last[1]:
            last[1] = max(last[1], cur[1])
        else:
            merged.append(cur)

    return merged
```