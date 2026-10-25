```python
def minutes_between(start_time: str, end_time: str) -> int:
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))
    
    start_total = start_hour * 60 + start_minute
    end_total = end_hour * 60 + end_minute
    
    if end_total <= start_total:
        end_total += 24 * 60
        
    return end_total - start_total
```