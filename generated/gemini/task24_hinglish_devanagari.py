```python
from collections import Counter


def second_most_common(s: str) -> str | None:
    filtered_chars = [c for c in s if c != " "]

    if len(set(filtered_chars)) < 2:
        return None

    counts = Counter(filtered_chars)

    sorted_chars = sorted(
        counts.keys(),
        key=lambda x: (-counts[x], filtered_chars.index(x)),
    )

    return sorted_chars[1]
```