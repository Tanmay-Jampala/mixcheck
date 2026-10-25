```python
def second_most_common(s: str):
    cleaned = [c for c in s if c != ' ']
    if len(set(cleaned)) < 2:
        return None

    counts = {}
    for c in cleaned:
        counts[c] = counts.get(c, 0) + 1

    sorted_chars = sorted(counts.keys(), key=lambda x: (-counts[x], cleaned.index(x)))
    return sorted_chars[1]
```