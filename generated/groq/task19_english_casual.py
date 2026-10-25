```python
def minutes_between(start: str, end: str) -> int:
    """Return the number of minutes from `start` to `end`.
    Times are 24‑hour strings "HH:MM". If `end` is earlier than `start`,
    it is considered to be on the next day.
    """
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    s = to_minutes(start)
    e = to_minutes(end)

    # If end is earlier (or equal) we wrap to the next day
    if e <= s:
        e += 24 * 60

    return e - s
```