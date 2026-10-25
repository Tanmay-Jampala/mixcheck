```python
from collections import Counter

def second_most_common(s: str):
    # Remove spaces for counting and uniqueness check
    filtered = [c for c in s if c != ' ']
    if len(set(filtered)) < 2:
        return None

    freq = Counter(filtered)

    # Record first occurrence index (ignoring spaces)
    first_index = {}
    for idx, c in enumerate(s):
        if c == ' ':
            continue
        if c not in first_index:
            first_index[c] = idx

    # Sort by frequency descending, then by first appearance
    sorted_chars = sorted(freq.keys(), key=lambda c: (-freq[c], first_index[c]))

    return sorted_chars[1] if len(sorted_chars) >= 2 else None
```