```python
def second_most_common(s: str):
    freq = {}
    first_idx = {}

    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in freq:
            freq[ch] = 0
            first_idx[ch] = i
        freq[ch] += 1

    # less than two distinct characters
    if len(freq) < 2:
        return None

    # sort by frequency descending, then by first appearance ascending
    sorted_chars = sorted(freq.items(),
                          key=lambda kv: (-kv[1], first_idx[kv[0]]))

    # second element's character
    return sorted_chars[1][0]
```