```python
def second_most_common(s: str):
    """
    Return the character that appears the second most often in `s`.
    - Spaces are ignored.
    - Upper‑ and lower‑case are treated as distinct.
    - If two characters have the same frequency, the one that appears
      earlier in the original string ranks higher.
    - If there are fewer than two distinct characters (ignoring spaces),
      return None.
    """
    counts = {}
    first_pos = {}

    for idx, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in counts:
            counts[ch] = 0
            first_pos[ch] = idx
        counts[ch] += 1

    if len(counts) < 2:
        return None

    # Build a list of (char, count, first_position) and sort
    ranked = sorted(
        ((ch, cnt, first_pos[ch]) for ch, cnt in counts.items()),
        key=lambda x: (-x[1], x[2])   # descending count, then ascending first index
    )

    # The second element in the sorted list is the answer
    return ranked[1][0]
```