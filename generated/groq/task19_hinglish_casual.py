```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.

    Parameters
    ----------
    start : str
        Time in 24‑hour "HH:MM" format.
    end : str
        Time in 24‑hour "HH:MM" format. If it is earlier than `start`,
        it is considered to be on the next day.

    Returns
    -------
    int
        Minutes between the two times.
    """
    # Convert "HH:MM" → total minutes since midnight
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    start_min = to_minutes(start)
    end_min   = to_minutes(end)

    # If end is earlier, treat it as next day
    if end_min < start_min:
        end_min += 24 * 60

    return end_min - start_min


# Example usage
if __name__ == "__main__":
    print(minutes_between("22:15", "01:45"))  # 210 minutes (3h30m next day)
    print(minutes_between("09:00", "12:30"))  # 210 minutes
```
This function works purely with integer arithmetic, so it’s fast and has no external dependencies.