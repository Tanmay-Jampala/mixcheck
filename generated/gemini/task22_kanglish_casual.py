```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Start prakara sort maadu
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current

        # Touch aadru overlap antha treat maadu (prev_end >= curr_start)
        if prev_end >= curr_start:
            merged[-1][1] = max(prev_end, curr_end)
        else:
            merged.append(current)

    return merged
```