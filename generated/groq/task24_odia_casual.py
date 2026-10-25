```python
def second_most_common(s: str):
    # Count frequencies and remember first occurrence index
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

    # Sort by (-frequency, first occurrence)
    sorted_chars = sorted(freq.items(),
                          key=lambda kv: (-kv[1], first_idx[kv[0]]))

    # Return the character at second position
    return sorted_chars[1][0]
```