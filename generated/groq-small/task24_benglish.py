```python
def second_most_common(s: str):
    # Count characters and remember first occurrence index
    counts = {}
    first_index = {}
    for idx, ch in enumerate(s):
        if ch == ' ':
            continue
        counts[ch] = counts.get(ch, 0) + 1
        if ch not in first_index:
            first_index[ch] = idx

    # Need at least two distinct characters
    if len(counts) < 2:
        return None

    # Sort by frequency descending, then by first appearance ascending
    sorted_chars = sorted(
        counts.keys(),
        key=lambda c: (-counts[c], first_index[c])
    )

    # Return the second element
    return sorted_chars[1]
```