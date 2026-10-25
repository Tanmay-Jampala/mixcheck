```python
def second_most_common(s: str):
    # Count frequencies and remember first occurrence index (ignoring spaces)
    freq = {}
    first_idx = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in freq:
            freq[ch] = 0
            first_idx[ch] = i
        freq[ch] += 1

    # If fewer than 2 distinct characters, return None
    if len(freq) < 2:
        return None

    # Sort by descending frequency, then by first appearance index
    sorted_chars = sorted(
        freq.items(),
        key=lambda item: (-item[1], first_idx[item[0]])
    )

    # Return the character at rank 2
    return sorted_chars[1][0]
```