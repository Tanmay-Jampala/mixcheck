**Python function – `merge_intervals`**

```python
from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge a list of intervals.

    *   Each interval is a tuple / list ``(start, end)`` where ``start <= end``.
    *   Intervals that overlap **or just touch** (e.g. [1,3] and [3,5])
        are considered a single merged interval.
    *   The result is sorted by the start value.

    Parameters
    ----------
    intervals : List[Tuple[int, int]]
        List of intervals to be merged.

    Returns
    -------
    List[Tuple[int, int]]
        A new list containing the merged intervals, sorted by start.

    Example
    -------
    >>> merge_intervals([(1, 3), (2, 6), (8, 10), (10, 12), (15, 18)])
    [(1, 6), (8, 12), (15, 18)]
    """
    if not intervals:
        return []

    # 1️⃣  Sort by the start value (and by end as tie‑breaker)
    sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

    merged: List[Tuple[int, int]] = [sorted_intervals[0]]

    for cur_start, cur_end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]

        # 2️⃣  Overlap / touch condition:
        #     if the current start is <= last_end, they belong together.
        if cur_start <= last_end:                     # <-- touch counts as overlap
            # Extend the previous interval only if needed
            merged[-1] = (last_start, max(last_end, cur_end))
        else:
            # No overlap → start a new interval
            merged.append((cur_start, cur_end))

    return merged
```

---

### ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?

1. **ಸಾರ್ಟ್** – ಮೊದಲಿಗೆ ಎಲ್ಲಾ ಇಂಟರ್ವೆಲ್‌ಗಳನ್ನು `start` ಆಧರಿಸಿ ಏರಿಕ್ರಮದಲ್ಲಿ (ascending) ಸರಿಸು.  
   ಇದರಿಂದ ನಾವು ಯಾವಾಗಲೂ “ಹಿಂದಿನ” ಇಂಟರ್ವೆಲ್‌ನ್ನು ನೋಡಿದಾಗ ಅದರ `end` ಮೌಲ್ಯವನ್ನು ತಿಳಿದುಕೊಳ್ಳಬಹುದು.

2. **ಇಟರೇಟ್** – ಮೊದಲ ಇಂಟರ್ವೆಲ್ ಅನ್ನು `merged` ಪಟ್ಟಿಗೆ ಹಾಕಿ, ನಂತರ ಉಳಿದ ಇಂಟರ್ವೆಲ್‌ಗಳ ಮೇಲೆ ಲೂಪ್ ನಡೆಸಿ.  
   - ಪ್ರಸ್ತುತ ಇಂಟರ್ವೆಲ್‌ (`cur_start, cur_end`) ಮತ್ತು ಕೊನೆಯ ಮರ್ಜ್ ಆಗಿರುವ ಇಂಟರ್ವೆಲ್‌ (`last_start, last_end`) ಅನ್ನು ಹೋಲಿಸಿ.  
   - **ಸಂಪರ್ಕ / ಸ್ಪರ್ಶ**: `cur_start <= last_end` ಆಗಿದ್ದರೆ, ಅವು ಒಟ್ಟಿಗೆ ಒಂದೇ ಇಂಟರ್ವೆಲ್ ಆಗಬೇಕು.  
     - ಹೊಸ `end` ಅನ್ನು `max(last_end, cur_end)` ಆಗಿ ನವೀಕರಿಸಿ.  
   - ಇಲ್ಲದಿದ್ದರೆ (ಅಂದರೆ `cur_start > last_end`) – ಹೊಸ, ಪ್ರತ್ಯೇಕ ಇಂಟರ್ವೆಲ್ ಆಗಿ `merged` ಗೆ ಸೇರಿಸಿ.

3. **ಫಲಿತಾಂಶ** – `merged` ಪಟ್ಟಿಯೇ ಅಂತಿಮವಾಗಿ ಮರ್ಜ್ ಆಗಿರುವ, `start` ಪ್ರಕಾರ ಸರಿಯಾದ ಇಂಟರ್ವೆಲ್‌ಗಳ ಪಟ್ಟಿಯಾಗಿದೆ.

---

### ಕೆಲವು ಹೆಚ್ಚುವರಿ ಉದಾಹರಣೆಗಳು

```python
# 1. ಸ್ಪರ್ಶಿಸುವ ಇಂಟರ್ವೆಲ್‌ಗಳು ಕೂಡ ಮರ್ಜ್ ಆಗುತ್ತವೆ
print(merge_intervals([(1, 2), (2, 4), (5, 7)]))
# → [(1, 4), (5, 7)]

# 2. ಪೂರ್ಣವಾಗಿ ಒಳಗೊಳ್ಳುವ ಇಂಟರ್ವೆಲ್‌ಗಳು
print(merge_intervals([(1, 10), (2, 3), (4, 8)]))
# → [(1, 10)]

# 3. ಖಾಲಿ ಇನ್‌ಪುಟ್
print(merge_intervals([]))
# → []

# 4. ಒಂದೇ ಇಂಟರ್ವೆಲ್
print(merge_intervals([(5, 9)]))
# → [(5, 9)]
```

---

### ಬಳಕೆ

```python
intervals = [(6, 8), (1, 3), (2, 5), (10, 12), (9, 10)]
merged = merge_intervals(intervals)
print(merged)          # [(1, 5), (6, 8), (9, 12)]
```

ಈ ಫಂಕ್ಷನ್ O(N log N) ಸಮಯದಲ್ಲಿ (ಸಾರ್ಟ್) ಮತ್ತು O(N) ಹೆಚ್ಚುವರಿ ಸ್ಥಳದಲ್ಲಿ (ಫಲಿತಾಂಶ) ಕೆಲಸ ಮಾಡುತ್ತದೆ, ಆದ್ದರಿಂದ ದೊಡ್ಡ ಡೇಟಾಸೆಟ್‌ಗಳಿಗೂ ಪರಿಣಾಮಕಾರಿಯಾಗಿದೆ.