```python
def second_most_common(s: str):
    freq = {}
    first = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        freq[ch] = freq.get(ch, 0) + 1
        if ch not in first:
            first[ch] = i

    if len(freq) < 2:
        return None

    # Sort by descending frequency, then by first occurrence index
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], first[x[0]]))
    return sorted_chars[1][0]
```