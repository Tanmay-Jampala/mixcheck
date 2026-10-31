**Python function**

```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from *start* to *end*.

    Parameters
    ----------
    start : str
        Start time in 24‑hour format "HH:MM".
    end : str
        End time in 24‑hour format "HH:MM".

    Returns
    -------
    int
        Minutes between the two times.  
        If *end* is earlier than *start*, it is assumed to be on the next day.

    Examples
    --------
    >>> minutes_between("09:15", "10:45")
    90
    >>> minutes_between("23:30", "00:15")
    45
    >>> minutes_between("12:00", "12:00")
    0
    """
    # Convert "HH:MM" to minutes since midnight
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    start_min = sh * 60 + sm
    end_min   = eh * 60 + em

    # If end is earlier, it means the next day
    if end_min < start_min:
        end_min += 24 * 60

    return end_min - start_min
```

**How it works**

1. Split each string into hours and minutes and convert to integers.  
2. Compute the total minutes from midnight for both times.  
3. If the end time is earlier than the start time, add 24 × 60 minutes to the end time to account for the next day.  
4. Return the difference.

This function handles all edge cases (same time → 0 minutes, overnight wrap‑around, etc.) and works with any valid 24‑hour `"HH:MM"` strings.