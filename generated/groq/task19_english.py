```python
def minutes_between(start: str, end: str) -> int:
    """Return the number of minutes from start to end.
    
    Times are given in 24‑hour "HH:MM" format. If end is earlier than start,
    it is considered to be on the next day.
    """
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    start_min = to_minutes(start)
    end_min = to_minutes(end)

    diff = end_min - start_min
    if diff < 0:
        diff += 24 * 60  # wrap to next day
    return diff
```