```python
def minutes_between(start: str, end: str) -> int:
    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, end.split(':'))
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if t2 < t1:          # next day
        t2 += 24 * 60
    return t2 - t1
```