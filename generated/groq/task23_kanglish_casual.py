Here’s a compact, well‑documented Python function that does exactly what you described.

```python
def grade_from_marks(marks: int) -> str:
    """
    Convert a numeric mark into a letter grade.

    Parameters
    ----------
    marks : int
        The score obtained. Must be between 0 and 100 (inclusive).

    Returns
    -------
    str
        The corresponding grade:
        * 90‑100 → "A"
        * 75‑89  → "B"
        * 60‑74  → "C"
        * 40‑59  → "D"
        * 0‑39   → "F"
        * otherwise → "Invalid"

    Examples
    --------
    >>> grade_from_marks(92)
    'A'
    >>> grade_from_marks(67)
    'C'
    >>> grade_from_marks(-5)
    'Invalid'
    """
    # First handle out‑of‑range values
    if marks < 0 or marks > 100:
        return "Invalid"

    # Determine the grade based on the defined intervals
    if 90 <= marks <= 100:
        return "A"
    elif 75 <= marks <= 89:
        return "B"
    elif 60 <= marks <= 74:
        return "C"
    elif 40 <= marks <= 59:
        return "D"
    else:                     # 0 <= marks <= 39
        return "F"


# ---- Quick sanity test ----
if __name__ == "__main__":
    test_cases = [95, 80, 70, 45, 20, -3, 105]
    for m in test_cases:
        print(f"Marks: {m:3} → Grade: {grade_from_marks(m)}")
```

**Explanation**

1. **Range check** – The first `if` catches any value below 0 or above 100 and returns `"Invalid"`.
2. **Grade mapping** – The subsequent `elif` blocks follow the exact intervals you specified.
3. **Fallback** – The final `else` covers the remaining valid range (0‑39) and returns `"F"`.

You can drop the function into any script or module and call `grade_from_marks(your_mark)` to get the appropriate grade string.