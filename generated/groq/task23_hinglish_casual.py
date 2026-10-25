```python
def grade_from_marks(marks: int) -> str:
    """
    Return a grade based on the given marks.

    Grades:
        90‑100 : "A"
        75‑89  : "B"
        60‑74  : "C"
        40‑59  : "D"
        0‑39   : "F"
        otherwise (marks < 0 or marks > 100) : "Invalid"
    """
    if not isinstance(marks, (int, float)):
        return "Invalid"

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