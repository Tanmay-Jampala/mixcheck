Below is a compact, well‑documented implementation of **`merge_intervals`** that satisfies all the requirements you listed:

* **Input** – a list of intervals, each interval being a two‑element list or tuple `[start, end]`.
* **Behaviour** –  
  * Intervals that **overlap** (`a.start ≤ b.end` and `b.start ≤ a.end`) are merged.  
  * Intervals that **touch** (`a.end == b.start` or `b.end == a.start`) are also treated as overlapping and merged.  
* **Output** – a new list of merged intervals, sorted by the start value.

```python
from typing import List, Tuple, Union

Interval = Union[List[int], Tuple[int, int]]


def merge_intervals(intervals: List[Interval]) -> List[List[int]]:
    """
    Merge a collection of possibly‑overlapping or touching intervals.

    Parameters
    ----------
    intervals : List[Interval]
        A list where each element is a 2‑item list/tuple ``[start, end]``.
        ``start`` may be greater than ``end`` – the function will normalise
        them to ``[min, max]`` before processing.

    Returns
    -------
    List[List[int]]
        A new list of merged intervals, sorted by the start coordinate.
        Each interval is returned as a list ``[start, end]`` (inclusive).

    Examples
    --------
    >>> merge_intervals([[1, 3], [2, 6], [8, 10], [10, 12]])
    [[1, 6], [8, 12]]

    >>> merge_intervals([[5, 1], [2, 4], [4, 7]])
    [[1, 7]]
    """
    if not intervals:
        return []

    # ------------------------------------------------------------------
    # 1️⃣ Normalise each interval so that start <= end.
    # ------------------------------------------------------------------
    norm = [[min(s, e), max(s, e)] for s, e in intervals]

    # ------------------------------------------------------------------
    # 2️⃣ Sort by the start coordinate (required output order).
    # ------------------------------------------------------------------
    norm.sort(key=lambda x: x[0])

    merged: List[List[int]] = []
    cur_start, cur_end = norm[0]

    for start, end in norm[1:]:
        # If the current interval overlaps or touches the previous one,
        # extend the previous interval.
        if start <= cur_end:          # <-- overlap OR touch (end == start)
            cur_end = max(cur_end, end)
        else:
            # No overlap – push the finished interval and start a new one.
            merged.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    # Append the last interval that is still in the buffer.
    merged.append([cur_start, cur_end])
    return merged


# ----------------------------------------------------------------------
# Simple sanity‑check when the file is run directly.
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [10, 12]], [[1, 6], [8, 12]]),
        ([[5, 1], [2, 4], [4, 7]], [[1, 7]]),
        ([], []),
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
        ([[1, 5], [5, 10], [10, 15]], [[1, 15]]),  # touching intervals
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        out = merge_intervals(inp)
        assert out == expected, f"Test {i} failed: got {out}, expected {expected}"
    print("All demo tests passed ✅")
```

### How it works (step‑by‑step)

| Step | What we do | Why |
|------|------------|-----|
| **1️⃣ Normalise** | Convert each interval to `[min(start,end), max(start,end)]`. | Guarantees the algorithm works even if a user supplies `[end, start]`. |
| **2️⃣ Sort** | `norm.sort(key=lambda x: x[0])`. | Merging works in a single left‑to‑right pass only when intervals are ordered by their start. |
| **3️⃣ Scan & merge** | Keep a “current” interval (`cur_start`, `cur_end`). For each next interval:<br>• If `next.start ≤ cur_end` → they overlap **or** touch → extend `cur_end`.<br>• Else → push the current interval to `merged` and start a new current interval. | The condition `start <= cur_end` treats touching intervals (`cur_end == start`) as overlapping, exactly as you asked. |
| **4️⃣ Flush** | After the loop, append the last buffered interval. | The final interval would otherwise be left out. |

### Complexity

* **Time** – `O(n log n)` because of the sorting step (`n` = number of intervals).  
* **Space** – `O(n)` for the output list (in‑place merging isn’t possible while preserving the original order).

Feel free to copy‑paste the function into your project. If you need any tweaks (e.g., handling floating‑point intervals, returning tuples instead of lists, etc.) just let me know!