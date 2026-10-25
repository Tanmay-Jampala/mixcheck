```python
def grade_from_marks(marks: int) -> str:
    """
    Convert a numeric mark to a letter grade.

    Parameters
    ----------
    marks : int
        Whole‑number mark (expected 0‑100).

    Returns
    -------
    str
        Grade according to the following scale:
        - 90‑100 : "A"
        - 75‑89  : "B"
        - 60‑74  : "C"
        - 40‑59  : "D"
        - 0‑39   : "F"
        - otherwise : "Invalid"
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