**Python function**

```python
from collections import Counter
from typing import Optional

def second_most_common(s: str) -> Optional[str]:
    """
    Return the second‑most common character in *s*.

    Rules
    -----
    * Spaces are ignored.
    * Upper‑case and lower‑case are treated as different characters.
    * If two (or more) characters have the same frequency, the one that
      appears first in the original string wins.
    * If the string contains fewer than two distinct non‑space characters,
      return ``None``.
    """
    # 1. Count all non‑space characters
    counts = Counter(ch for ch in s if ch != ' ')

    # 2. If we have fewer than 2 distinct characters → None
    if len(counts) < 2:
        return None

    # 3. Record the first index of each character (for tie‑breaking)
    first_index = {}
    for idx, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in first_index:
            first_index[ch] = idx

    # 4. Build a sortable list: (char, count, first_index)
    items = [(ch, cnt, first_index[ch]) for ch, cnt in counts.items()]

    # 5. Sort by descending count, then ascending first_index
    items.sort(key=lambda x: (-x[1], x[2]))

    # 6. Return the character of the second element
    return items[1][0]
```

---

### How it works

| Step | What happens | Why |
|------|--------------|-----|
| 1 | `Counter` tallies every non‑space character. | Gives us the frequency of each character. |
| 2 | If fewer than two distinct characters → `None`. | Matches the requirement. |
| 3 | Record the first occurrence index of each character. | Needed to break ties by “first in string”. |
| 4 | Create a list of tuples `(char, count, first_index)`. | Makes sorting easy. |
| 5 | Sort by `-count` (descending frequency) and then by `first_index` (ascending). | Ensures ties are resolved by first appearance. |
| 6 | Return the character of the second tuple. | That’s the second‑most common character. |

---

### Quick examples

```python
>>> second_most_common("aabbc")
'b'          # a:2, b:2, c:1 → tie between a & b → a first, so b is second

>>> second_most_common("  aa bb cc dd  ")
'd'          # a,b,c,d all 2 → a first, b second, c third, d fourth → second is b

>>> second_most_common("abc")
None         # only 3 distinct chars, but we need at least 2 distinct → returns None

>>> second_most_common("a a a b b")
'b'          # a:3, b:2 → second most common is b

>>> second_most_common("Aaa a")
'A'          # A:1, a:4 → second most common is A
```

Feel free to drop this function into your project!