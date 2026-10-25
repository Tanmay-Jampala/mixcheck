```python
from collections import Counter


def second_most_common(s):
    s = s.replace(" ", "")
    counts = Counter(s)
    if len(counts) < 2:
        return None

    first_seen = {}
    for i, char in enumerate(s):
        if char not in first_seen:
            first_seen[char] = i

    sorted_chars = sorted(counts.keys(), key=lambda x: (-counts[x], first_seen[x]))
    return sorted_chars[1]
```