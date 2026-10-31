Here’s a compact, self‑contained implementation that follows the specification:

```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.

    Both arguments are strings in 24‑hour "HH:MM" format.
    If `end` is earlier than `start`, it is interpreted as occurring on the next day.

    Examples
    --------
    >>> minutes_between("09:30", "11:00")
    90
    >>> minutes_between("23:15", "01:45")   # next‑day wrap‑around
    150
    """
    # Helper: convert "HH:MM" → total minutes since midnight
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError(f"Invalid time string: {t!r}")
        return h * 60 + m

    start_min = to_minutes(start)
    end_min   = to_minutes(end)

    # If end is earlier, we add a full day (24*60 minutes) to it.
    if end_min < start_min:
        end_min += 24 * 60

    return end_min - start_min


# ----------------------------------------------------------------------
# Quick sanity‑check (you can delete or comment this block in production)
if __name__ == "__main__":
    test_cases = [
        ("00:00", "00:00", 0),
        ("09:30", "11:00", 90),
        ("23:15", "01:45", 150),
        ("12:00", "12:00", 0),
        ("18:45", "18:30", 1415),  # next day: 23h45m = 1415 min
    ]

    for s, e, expected in test_cases:
        result = minutes_between(s, e)
        assert result == expected, f"{s}->{e}: expected {expected}, got {result}"
    print("All tests passed.")
```

**Explanation**

1. **Parsing** – `to_minutes` splits the `"HH:MM"` string, converts the hour and minute parts to integers, validates the range, and returns the total minutes since midnight (`hour * 60 + minute`).

2. **Wrap‑around handling** – After converting both times, we compare them. If `end` is earlier (`end_min < start_min`), we treat it as occurring on the next day by adding `24 * 60` minutes (the length of a full day) to `end_min`.

3. **Result** – The difference `end_min - start_min` is the desired number of minutes.

The function raises a `ValueError` for malformed inputs, making debugging easier. Feel free to integrate it into a larger codebase or adapt the validation logic to your needs.