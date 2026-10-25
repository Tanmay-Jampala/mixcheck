```python
def minutes_between(start: str, end: str) -> int:
    """Return the number of minutes from start to end.
    Times are given in 24‑hour 'HH:MM' format. If end is earlier than start,
    it is considered to be on the next day.
    """
    h1, m1 = map(int, start.split(":"))
    h2, m2 = map(int, end.split(":"))
    start_min = h1 * 60 + m1
    end_min = h2 * 60 + m2

    diff = end_min - start_min
    if diff < 0:               # end is on the next day
        diff += 24 * 60
    return diff
```