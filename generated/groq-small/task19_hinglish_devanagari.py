```python
def minutes_between(start: str, end: str) -> int:
    """Return the number of minutes from start to end, treating end as next day if it is earlier."""
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    start_minutes = sh * 60 + sm
    end_minutes = eh * 60 + em
    if end_minutes < start_minutes:
        end_minutes += 24 * 60
    return end_minutes - start_minutes
```