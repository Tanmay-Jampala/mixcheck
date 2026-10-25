```python
def minutes_between(start: str, end: str) -> int:
    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, end.split(':'))
    minutes_start = h1 * 60 + m1
    minutes_end = h2 * 60 + m2
    diff = minutes_end - minutes_start
    if diff < 0:
        diff += 24 * 60
    return diff
```