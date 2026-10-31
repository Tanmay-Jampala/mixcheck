Here’s a concise implementation of the requested function:

```python
def grade_from_marks(marks):
    """
    Convert a numeric mark (0‑100) to a letter grade.

    Parameters
    ----------
    marks : int or float
        The score to be graded.

    Returns
    -------
    str
        The corresponding grade:
        - "A" for 90‑100
        - "B" for 75‑89
        - "C" for 60‑74
        - "D" for 40‑59
        - "F" for 0‑39
        - "Invalid" for values outside 0‑100
    """
    # First, check for out‑of‑range values
    if marks < 0 or marks > 100:
        return "Invalid"

    # Determine the grade based on the defined intervals
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:               # marks is between 0 and 39 inclusive
        return "F"


# Example usage
if __name__ == "__main__":
    test_scores = [95, 82, 67, 45, 23, -5, 105]
    for s in test_scores:
        print(f"Marks: {s:3} → Grade: {grade_from_marks(s)}")
```

**Explanation**

1. **Input validation** – The function first checks whether `marks` lies outside the permissible range (0‑100). If so, it returns `"Invalid"`.
2. **Grade determination** – The remaining `if/elif/else` chain checks the score against the upper bounds of each grade interval, starting from the highest grade. Because the conditions are evaluated in order, once a condition matches, the corresponding grade is returned.
3. **Flexibility** – The function accepts both integers and floats, so values like `89.5` will correctly be graded as `"B"`.

Feel free to integrate this function into your larger codebase or adapt the grade boundaries as needed.