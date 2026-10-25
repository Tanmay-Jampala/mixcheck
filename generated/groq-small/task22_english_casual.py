```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Ensure each interval is a mutable list and sort by start
    intervals = sorted([list(x) for x in intervals], key=lambda x: x[0])

    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:          # overlapping or touching
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```