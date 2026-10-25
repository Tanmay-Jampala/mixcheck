```python
def second_most_common(s: str):
    # Count frequencies ignoring spaces
    freq = {}
    first_index = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        freq[ch] = freq.get(ch, 0) + 1
        if ch not in first_index:
            first_index[ch] = i

    if len(freq) < 2:
        return None

    # Sort by frequency descending, then by first appearance ascending
    sorted_chars = sorted(freq.keys(), key=lambda c: (-freq[c], first_index[c]))
    return sorted_chars[1]
```