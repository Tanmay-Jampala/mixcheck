def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start value
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = [sorted_intervals[0].copy()]
    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # overlapping or touching
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged