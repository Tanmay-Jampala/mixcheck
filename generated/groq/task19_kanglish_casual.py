Here’s a compact, pure‑Python implementation that follows exactly what you described:

```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from *start* to *end*.
    
    Both arguments must be strings in 24‑hour “HH:MM” format.
    If *end* is earlier than *start* it is treated as a time on the
    following day.

    Example
    -------
    >>> minutes_between("09:30", "12:15")
    165
    >>> minutes_between("22:10", "01:45")   # next‑day case
    215
    """
    # ---- 1️⃣  Parse the two strings into hour / minute integers ----
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))

    # ---- 2️⃣  Convert each time to “minutes since midnight” ----
    start_min = sh * 60 + sm
    end_min   = eh * 60 + em

    # ---- 3️⃣  If end is earlier, add 24 h (1440 min) to treat it as next day ----
    if end_min < start_min:
        end_min += 24 * 60   # 1440 minutes

    # ---- 4️⃣  The difference is the answer ----
    return end_min - start_min


# ----------------------------------------------------------------------
# Quick sanity‑check (you can delete or comment this block in production)
if __name__ == "__main__":
    tests = [
        ("09:30", "12:15", 165),
        ("22:10", "01:45", 215),   # next‑day
        ("00:00", "00:00", 0),
        ("23:59", "00:01", 2),     # next‑day, crossing midnight
    ]

    for s, e, expected in tests:
        result = minutes_between(s, e)
        print(f"{s} → {e} = {result} min  {'✅' if result == expected else '❌'}")
```

### How it works
1. **Parsing** – `split(":")` gives the hour and minute parts, which we turn into integers.
2. **Normalization** – `hour * 60 + minute` converts each time to “minutes since midnight”.
3. **Cross‑midnight handling** – If the end‑time’s minute count is smaller than the start‑time’s, we add a full day (1440 minutes) to the end‑time. This makes the interval span into the next day.
4. **Result** – The simple subtraction yields the number of minutes between the two moments.

The function works for any valid `"HH:MM"` strings (00 ≤ HH ≤ 23, 00 ≤ MM ≤ 59). If you need stricter validation you can add a `try/except` block or use `datetime.strptime`, but the above keeps it lightweight and fast.