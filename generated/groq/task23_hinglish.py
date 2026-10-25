```python
def grade_from_marks(marks: int) -> str:
    """Return grade based on numeric marks.

    Args:
        marks: Integer score of the student.

    Returns:
        A single-letter grade ("A", "B", "C", "D", "F") or "Invalid"
        if the marks are outside the 0‑100 range.
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