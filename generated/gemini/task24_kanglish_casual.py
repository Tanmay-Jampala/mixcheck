```python
from collections import Counter


def second_most_common(s):
    # Spaces ignore maadu
    s = s.replace(" ", "")

    if len(set(s)) < 2:
        return None

    # Count frequencies, maintaining original order of first appearance
    counts = Counter(s)

    # Sort by frequency descending (-v), then by first appearance in string (s.find(k))
    sorted_chars = sorted(counts.keys(), key=lambda x: (-counts[x], s.find(x)))

    return sorted_chars[1]
```