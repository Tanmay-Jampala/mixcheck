```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.

    Parameters
    ----------
    start : str
        Start time in "HH:MM" 24‑hour format.
    end : str
        End time in "HH:MM" 24‑hour format. If `end` is earlier than `start`,
        it is considered to be on the next day.

    Returns
    -------
    int
        Minutes elapsed from start to end.
    """
    # Convert "HH:MM" to total minutes since midnight
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    start_min = to_minutes(start)
    end_min = to_minutes(end)

    # Difference modulo 24 hours (1440 minutes)
    diff = (end_min - start_min) % (24 * 60)
    return diff
```