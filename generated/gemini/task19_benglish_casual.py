```python
from datetime import datetime, timedelta


def minutes_between(start: str, end: str) -> int:
    fmt = "%H:%M"
    t1 = datetime.strptime(start, fmt)
    t2 = datetime.strptime(end, fmt)

    if t2 < t1:
        t2 += timedelta(days=1)

    return int((t2 - t1).total_seconds() // 60)
```