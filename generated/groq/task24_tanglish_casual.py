```python
def second_most_common(s: str):
    counts = {}
    first_idx = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in counts:
            counts[ch] = 0
            first_idx[ch] = i
        counts[ch] += 1

    if len(counts) < 2:
        return None

    # sort by descending frequency, then by first appearance index
    sorted_chars = sorted(counts, key=lambda c: (-counts[c], first_idx[c]))
    return sorted_chars[1]
```