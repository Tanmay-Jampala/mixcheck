```python
def second_most_common(s):
    from collections import Counter

    filtered_s = [c for c in s if c != " "]

    if len(set(filtered_s)) < 2:
        return None

    counts = Counter(filtered_s)

    sorted_chars = sorted(
        counts.keys(), key=lambda x: (-counts[x], filtered_s.index(x))
    )

    return sorted_chars[1]
```