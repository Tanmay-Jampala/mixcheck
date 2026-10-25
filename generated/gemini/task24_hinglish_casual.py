```python
from collections import Counter


def second_most_common(s):
    filtered = [c for c in s if c != " "]
    if len(set(filtered)) < 2:
        return None

    counts = Counter(filtered)
    order = {char: idx for idx, char in enumerate(filtered)}

    sorted_chars = sorted(
        counts.keys(), key=lambda x: (-counts[x], order[x])
    )

    return sorted_chars[1]
```