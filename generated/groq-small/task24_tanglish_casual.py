```python
def second_most_common(s: str):
    # Count frequencies and record first occurrence index
    freq = {}
    first_idx = {}
    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        freq[ch] = freq.get(ch, 0) + 1
        if ch not in first_idx:
            first_idx[ch] = i

    if len(freq) < 2:
        return None

    # Find most common character (tie‑break by first appearance)
    max_freq = max(freq.values())
    most_common = min(
        (ch for ch, f in freq.items() if f == max_freq),
        key=lambda ch: first_idx[ch]
    )

    # Remove the most common character
    del freq[most_common]

    # Find second most common (tie‑break by first appearance)
    second_max_freq = max(freq.values())
    second_common = min(
        (ch for ch, f in freq.items() if f == second_max_freq),
        key=lambda ch: first_idx[ch]
    )

    return second_common
```