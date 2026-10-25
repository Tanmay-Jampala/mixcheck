```python
def second_most_common(s: str):
    cleaned = s.replace(" ", "")
    if len(set(cleaned)) < 2:
        return None

    counts = {}
    for char in cleaned:
        counts[char] = counts.get(char, 0) + 1

    sorted_chars = sorted(counts.keys(), key=lambda x: (-counts[x], cleaned.index(x)))

    return sorted_chars[1]
```