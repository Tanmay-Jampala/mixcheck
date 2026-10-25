```python
def grade_from_marks(marks: int) -> str:
    if marks < 0 or marks > 100:
        return "Invalid"
    if 90 <= marks <= 100:
        return "A"
    if 75 <= marks <= 89:
        return "B"
    if 60 <= marks <= 74:
        return "C"
    if 40 <= marks <= 59:
        return "D"
    return "F"
```