```python
from datetime import datetime


def minutes_between(start: str, end: str) -> int:
    fmt = "%H:%M"
    t1 = datetime.strptime(start, fmt)
    t2 = datetime.strptime(end, fmt)

    diff = (t2 - t1).total_seconds() / 60
    if diff < 0:
        diff += 24 * 60

    return int(diff)
```