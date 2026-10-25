```python
from datetime import datetime, timedelta

def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.
    Times are given as "HH:MM" in 24‑hour format.
    If `end` is earlier than `start`, it is considered to be on the next day.
    """
    fmt = "%H:%M"
    t_start = datetime.strptime(start, fmt)
    t_end   = datetime.strptime(end,   fmt)

    delta = t_end - t_start
    if delta < timedelta(0):          # end is on the next day
        delta += timedelta(days=1)

    return int(delta.total_seconds() // 60)


# Example:
# print(minutes_between("23:45", "01:15"))  # 90
```