```python
def second_most_common(s: str):
    counts = {}
    first_index = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in counts:
            first_index[ch] = i
        counts[ch] = counts.get(ch, 0) + 1

    if len(counts) < 2:
        return None

    # Create a list of (char, count, first_index) tuples
    items = [(ch, cnt, first_index[ch]) for ch, cnt in counts.items()]
    # Sort by count descending, then by first appearance ascending
    items.sort(key=lambda x: (-x[1], x[2]))

    return items[1][0]
```