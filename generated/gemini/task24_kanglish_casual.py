```python
from collections import Counter


def second_most_common(s: str):
    s = s.replace(" ", "")
    if len(set(s)) < 2:
        return None
    counts = Counter(s)
    sorted_chars = sorted(
        counts.items(), key=lambda x: (-x[1], s.index(x[0]))
    )
    return sorted_chars[1][0]
```