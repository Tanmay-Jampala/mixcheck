```python
def grade_from_marks(marks: int) -> str:
    """
    Return a grade string based on the given marks.

    - 90  ≤ marks ≤ 100 : "A"
    - 75  ≤ marks ≤ 89  : "B"
    - 60  ≤ marks ≤ 74  : "C"
    - 40  ≤ marks ≤ 59  : "D"
    - 0   ≤ marks ≤ 39  : "F"
    - otherwise        : "Invalid"
    """
    if not isinstance(marks, (int, float)):
        return "Invalid"

    # Convert to integer for comparison (e.g., 89.5 should be treated as 89)
    marks = int(marks)

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