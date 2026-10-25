```python
def minutes_between(start: str, end: str) -> int:
    """Return the number of minutes from start to end.
    If end is earlier than start, it is considered to be on the next day."""
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    start_min = sh * 60 + sm
    end_min = eh * 60 + em
    if end_min <= start_min:
        end_min += 24 * 60
    return end_min - start_min
```