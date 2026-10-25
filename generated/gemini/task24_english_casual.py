```python
from collections import Counter


def second_most_common(s: str):
    filtered = [c for c in s if c != " "]
    if len(set(filtered)) < 2:
        return None
    counts = Counter(filtered)
    ranked = sorted(
        counts.keys(), key=lambda c: (-counts[c], filtered.index(c))
    )
    return ranked[1]
```