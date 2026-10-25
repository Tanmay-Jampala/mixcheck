```python
from datetime import datetime, timedelta


def minutes_between(start: str, end: str) -> int:
    fmt = "%H:%M"
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)

    if end_dt <= start_dt:
        end_dt += timedelta(days=1)

    return int((end_dt - start_dt).total_seconds() / 60)
```