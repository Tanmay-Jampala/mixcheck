```python
def grade_from_marks(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 75 <= marks <= 89:
        return "B"
    elif 60 <= marks <= 74:
        return "C"
    elif 40 <= marks <= 59:
        return "D"
    elif 0 <= marks <= 39:
        return "F"
    else:
        return "Invalid"
```