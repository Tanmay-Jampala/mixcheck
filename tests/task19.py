# tests/task19.py
# Task: minutes from start to end, end may be the next day
FUNCTION = "minutes_between"

CASES = [
    (["09:00", "10:30"], 90),  # same day
    (["23:30", "00:15"], 45),  # the example: across midnight
    (["12:00", "12:00"], 0),  # same time
    (["00:00", "23:59"], 1439),  # almost a full day
    (["18:45", "06:15"], 690),  # evening to morning
]
