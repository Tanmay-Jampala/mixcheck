```python
def minutes_between(start: str, end: str) -> int:
    """Return the number of minutes from start to end.
    If end is earlier than start, it is considered to be on the next day.
    """
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    start_min = to_minutes(start)
    end_min = to_minutes(end)

    # If end is earlier, add 24 hours (1440 minutes)
    if end_min < start_min:
        end_min += 24 * 60

    return end_min - start_min
```