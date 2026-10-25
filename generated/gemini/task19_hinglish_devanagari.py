```python
from datetime import datetime, timedelta

def minutes_between(start_time: str, end_time: str) -> int:
    fmt = "%H:%M"
    t1 = datetime.strptime(start_time, fmt)
    t2 = datetime.strptime(end_time, fmt)
    
    if t2 <= t1:
        t2 += timedelta(days=1)
        
    diff = t2 - t1
    return int(diff.total_seconds() // 60)
```