**Python – `minutes_between(start, end)`**

```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from *start* to *end*.
    Both arguments must be strings in 24‑hour format "HH:MM".
    If *end* is earlier than *start*, the interval is assumed to cross midnight
    (i.e. *end* is on the next day).

    Examples
    --------
    >>> minutes_between("09:15", "10:45")
    90
    >>> minutes_between("23:30", "00:15")
    45
    >>> minutes_between("12:00", "12:00")
    0
    """
    # ---- 1. Parse the strings ---------------------------------------------
    try:
        h1, m1 = map(int, start.split(":"))
        h2, m2 = map(int, end.split(":"))
    except Exception as exc:
        raise ValueError("Both times must be in 'HH:MM' format") from exc

    # Basic sanity checks (optional but handy)
    if not (0 <= h1 < 24 and 0 <= m1 < 60):
        raise ValueError(f"Invalid start time: {start}")
    if not (0 <= h2 < 24 and 0 <= m2 < 60):
        raise ValueError(f"Invalid end time: {end}")

    # ---- 2. Convert to minutes since midnight -----------------------------
    start_min = h1 * 60 + m1
    end_min   = h2 * 60 + m2

    # ---- 3. Compute the difference ---------------------------------------
    diff = end_min - start_min
    if diff < 0:                     # crossed midnight
        diff += 24 * 60              # add 24 hours

    return diff
```

### How it works

1. **Parsing** – `split(":")` turns `"HH:MM"` into two integers.  
2. **Validation** – Optional checks ensure the hour is 0‑23 and the minute 0‑59.  
3. **Minutes‑since‑midnight** – Convert each time to a single integer (`hour*60 + minute`).  
4. **Difference** – Subtract the start from the end.  
   * If the result is negative, the end time is on the next day, so we add 24 × 60 minutes.  
5. **Return** – The final difference is the number of minutes between the two times.

Feel free to drop this function into your project or adapt it to your own style.