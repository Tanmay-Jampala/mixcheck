Here’s a compact, self‑contained implementation of the requested function:

```python
def grade_from_marks(marks: float) -> str:
    """
    Convert a numeric mark into a letter grade.

    Parameters
    ----------
    marks : float
        The numeric mark (expected to be in the range 0–100).

    Returns
    -------
    str
        The corresponding grade:
            - 90–100 : "A"
            - 75–89  : "B"
            - 60–74  : "C"
            - 40–59  : "D"
            - 0–39   : "F"
            - <0 or >100 : "Invalid"
    """
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

### Quick usage example

```python
for m in [95, 82, 68, 45, 30, -5, 105]:
    print(f"{m:>3} -> {grade_from_marks(m)}")
```

Output:

```
 95 -> A
 82 -> B
 68 -> C
 45 -> D
 30 -> F
 -5 -> Invalid
105 -> Invalid
```

The function uses a simple chain of `if` statements to test the ranges in descending order, ensuring that each mark falls into exactly one bucket. The type hint `float` allows both integer and floating‑point inputs.