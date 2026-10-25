**Python Function – `grade_from_marks`**

```python
def grade_from_marks(marks):
    """
    Convert a numeric mark into a letter grade.

    Parameters
    ----------
    marks : int | float
        The score obtained by a student.

    Returns
    -------
    str
        * "A"  – 90 ≤ marks ≤ 100
        * "B"  – 75 ≤ marks ≤ 89
        * "C"  – 60 ≤ marks ≤ 74
        * "D"  – 40 ≤ marks ≤ 59
        * "F"  – 0  ≤ marks ≤ 39
        * "Invalid" – any value outside 0–100

    Examples
    --------
    >>> grade_from_marks(95)
    'A'
    >>> grade_from_marks(82)
    'B'
    >>> grade_from_marks(55)
    'D'
    >>> grade_from_marks(-5)
    'Invalid'
    >>> grade_from_marks(101)
    'Invalid'
    """
    # Ensure the input is a number
    if not isinstance(marks, (int, float)):
        return "Invalid"

    # Check the bounds
    if marks < 0 or marks > 100:
        return "Invalid"

    # Determine the grade
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:          # marks is between 0 and 39
        return "F"
```

### How it works
1. **Type check** – If the input isn’t an `int` or `float`, we immediately return `"Invalid"`.
2. **Range check** – Marks outside the 0–100 interval are considered invalid.
3. **Grade mapping** – Using a series of `elif` statements (descending order) we map the numeric range to the corresponding letter grade.

Feel free to copy‑paste this function into your project or adapt it to your own grading scheme!