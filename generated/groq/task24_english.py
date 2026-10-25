```python
def second_most_common(s: str):
    # Count frequencies and record first occurrence index (ignoring spaces)
    freq = {}
    first_idx = {}
    for idx, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in freq:
            freq[ch] = 0
            first_idx[ch] = idx
        freq[ch] += 1

    # Need at least two distinct characters
    if len(freq) < 2:
        return None

    # Sort by descending frequency, then by ascending first occurrence index
    sorted_chars = sorted(
        freq.keys(),
        key=lambda c: (-freq[c], first_idx[c])
    )

    return sorted_chars[1]
```