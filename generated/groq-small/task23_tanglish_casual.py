```python
def grade_from_marks(marks):
    if marks < 0 or marks > 100:
        return "Invalid"
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"
```