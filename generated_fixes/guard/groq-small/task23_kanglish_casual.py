```python
def grade_from_marks(marks):
    if not isinstance(marks, (int, float)):
        return "Invalid"
    if marks < 0 or marks > 100:
        return "Invalid"
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
```