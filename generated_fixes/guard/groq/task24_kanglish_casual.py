```python
from typing import Optional

def second_most_common(s: str) -> Optional[str]:
    """
    Return the character that ranks second by frequency in the given string.

    Rules:
    - Spaces are ignored.
    - Upper‑case and lower‑case are treated as distinct characters.
    - When frequencies are equal, the character that appears earlier in the
      original string ranks higher.
    - If fewer than two distinct characters are present, return None.
    """
    counts = {}
    first_idx = {}

    for i, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in counts:
            counts[ch] = 0
            first_idx[ch] = i
        counts[ch] += 1

    if len(counts) < 2:
        return None

    # Sort by descending count, then by first occurrence index (ascending)
    sorted_chars = sorted(
        counts.keys(),
        key=lambda c: (-counts[c], first_idx[c])
    )

    return sorted_chars[1]
```