```python
def second_most_common(s: str):
    # Remove spaces but keep original order for tie‑breaking
    filtered = [ch for ch in s if ch != " "]

    # Not enough distinct characters
    if len(set(filtered)) < 2:
        return None

    # Count occurrences
    from collections import Counter
    counts = Counter(filtered)

    # Determine order of first appearance for each character
    first_index = {}
    for idx, ch in enumerate(s):
        if ch == " ":
            continue
        if ch not in first_index:
            first_index[ch] = idx

    # Build a list of (char, count, first_index) and sort
    # Primary: descending count
    # Secondary: ascending first appearance index (earlier wins on tie)
    sorted_chars = sorted(
        counts.items(),
        key=lambda item: (-item[1], first_index[item[0]])
    )

    # Return the character at rank 2 (index 1)
    return sorted_chars[1][0]
```