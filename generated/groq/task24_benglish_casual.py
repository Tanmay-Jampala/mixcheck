```python
def second_most_common(s: str):
    # count characters (ignore spaces) and remember first appearance index
    counts = {}
    first_idx = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in counts:
            counts[ch] = 0
            first_idx[ch] = i
        counts[ch] += 1

    # not enough distinct characters
    if len(counts) < 2:
        return None

    # sort by descending frequency, then by first appearance
    sorted_chars = sorted(
        counts.items(),
        key=lambda item: (-item[1], first_idx[item[0]])
    )

    # second element's character
    return sorted_chars[1][0]
```