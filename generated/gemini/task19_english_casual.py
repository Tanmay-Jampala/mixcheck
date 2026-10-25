```python
def minutes_between(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    
    start_minutes = sh * 60 + sm
    end_minutes = eh * 60 + em
    
    if end_minutes <= start_minutes:
        end_minutes += 24 * 60
        
    return end_minutes - start_minutes
```