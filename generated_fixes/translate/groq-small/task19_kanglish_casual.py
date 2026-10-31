Here’s a compact, well‑documented implementation that follows the specification:

```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from ``start`` to ``end``.
    
    Parameters
    ----------
    start : str
        Start time in 24‑hour format ``"HH:MM"``.
    end : str
        End time in 24‑hour format ``"HH:MM"``.
    
    Returns
    -------
    int
        Minutes elapsed from ``start`` to ``end``.  
        If ``end`` is earlier than ``start`` the calculation wraps to the next day.
    
    Examples
    --------
    >>> minutes_between("09:15", "10:45")
    90
    >>> minutes_between("23:30", "00:15")
    45
    >>> minutes_between("12:00", "12:00")
    0
    """
    # Helper to convert "HH:MM" → total minutes since midnight
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    start_min = to_minutes(start)
    end_min   = to_minutes(end)

    # If end is earlier, we assume it refers to the next day
    if end_min < start_min:
        end_min += 24 * 60

    return end_min - start_min
```

### Why this works

1. **Parsing** – `to_minutes` splits the string on `:` and converts the hour and minute parts to integers, then multiplies the hour by 60 and adds the minutes.
2. **Wrap‑around** – If the end time is chronologically before the start time, we add 24 × 60 minutes to the end value, effectively treating it as the next day.
3. **Difference** – The final subtraction gives the elapsed minutes.

Feel free to drop this function into your codebase or adapt it for additional validation if you need stricter input checks.