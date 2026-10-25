```python
def second_most_common(s):
    s = s.replace(" ", "")
    if len(set(s)) < 2:
        return None

    counts = {}
    order = {}
    for i, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        if char not in order:
            order[char] = i

    sorted_chars = sorted(
        counts.keys(), key=lambda x: (-counts[x], order[x])
    )

    return sorted_chars[1]
```