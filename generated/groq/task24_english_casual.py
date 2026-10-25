```python
def second_most_common(s: str):
    # Count frequencies and remember first appearance index
    freq = {}
    first_idx = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in freq:
            freq[ch] = 0
            first_idx[ch] = i
        freq[ch] += 1

    # Not enough distinct characters
    if len(freq) < 2:
        return None

    # Sort by frequency descending, then by first appearance ascending
    sorted_chars = sorted(
        freq.items(),
        key=lambda item: (-item[1], first_idx[item[0]])
    )

    # Return the character in second place
    return sorted_chars[1][0]
```