```python
def second_most_common(s: str):
    counts = {}
    first_index = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        counts[ch] = counts.get(ch, 0) + 1
        if ch not in first_index:
            first_index[ch] = i

    if len(counts) < 2:
        return None

    # Sort by frequency descending, then by first occurrence ascending
    sorted_chars = sorted(counts.keys(),
                          key=lambda c: (-counts[c], first_index[c]))

    return sorted_chars[1]
```