```python
from datetime import datetime, timedelta

def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.
    Times are given as "HH:MM" in 24‑hour format.
    If `end` is earlier than `start`, the interval is assumed to cross midnight.
    """
    fmt = "%H:%M"
    start_dt = datetime.strptime(start, fmt)
    end_dt   = datetime.strptime(end, fmt)

    # If end is earlier, add one day to end
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)

    delta = end_dt - start_dt
    return int(delta.total_seconds() // 60)
```

**Example usage**

```python
print(minutes_between("23:30", "00:15"))  # 45
print(minutes_between("08:00", "10:30"))  # 150
```
