```python
def minutes_between(start_time: str, end_time: str) -> int:
    start_hour, start_min = map(int, start_time.split(":"))
    end_hour, end_min = map(int, end_time.split(":"))
    
    start_total_minutes = start_hour * 60 + start_min
    end_total_minutes = end_hour * 60 + end_min
    
    if end_total_minutes < start_total_minutes:
        end_total_minutes += 24 * 60
        
    return end_total_minutes - start_total_minutes
```