```python
def minutes_between(start: str, end: str) -> int:
    """
    Return the number of minutes from `start` to `end`.
    Times are given as 24‑hour strings "HH:MM".
    If `end` is earlier than `start`, it is assumed to be on the next day.
    """
    # Convert "HH:MM" → total minutes since midnight
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    s = to_minutes(start)
    e = to_minutes(end)

    # If end is earlier, roll over to the next day (add 24h = 1440 minutes)
    if e < s:
        e += 24 * 60

    return e - s


# Example usage
if __name__ == "__main__":
    print(minutes_between("23:45", "00:15"))  # 30
    print(minutes_between("09:30", "12:00"))  # 150
    print(minutes_between("14:00", "14:00"))  # 0
```