```python
def grade_from_marks(marks: int) -> str:
    """Return the grade for a given whole‑number mark.

    Grades:
        90‑100 : "A"
        75‑89  : "B"
        60‑74  : "C"
        40‑59  : "D"
        0‑39   : "F"
    Returns "Invalid" for marks outside 0‑100.
    """
    if not isinstance(marks, int):
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