```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.
    Both arguments are strings in "HH:MM" 24‑hour format.
    If `end` is earlier than `start`, it is assumed to be on the next day.
    """
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    start_min = to_minutes(start)
    end_min = to_minutes(end)

    # Difference modulo one day (1440 minutes)
    return (end_min - start_min) % (24 * 60)
```