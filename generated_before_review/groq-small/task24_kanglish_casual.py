```python
from collections import Counter
from typing import Optional

def second_most_common(s: str) -> Optional[str]:
    """
    Return the second most common character in *s*.

    Rules
    -----
    * Spaces are ignored.
    * Upper‑case and lower‑case are treated as distinct characters.
    * If two (or more) characters have the same frequency, the one that
      appears first in the original string wins.
    * If the string contains fewer than two distinct non‑space characters,
      return ``None``.
    """
    # 1. Count frequencies, ignoring spaces
    freq = Counter(ch for ch in s if ch != ' ')

    # 2. If we have fewer than 2 distinct characters → None
    if len(freq) < 2:
        return None

    # 3. Record the first occurrence index of each character
    first_index = {}
    for idx, ch in enumerate(s):
        if ch == ' ':
            continue
        if ch not in first_index:
            first_index[ch] = idx

    # 4. Build a sortable list: (char, freq, first_index)
    items = [(ch, freq[ch], first_index[ch]) for ch in freq]

    # 5. Sort by frequency descending, then by first occurrence ascending
    items.sort(key=lambda x: (-x[1], x[2]))

    # 6. Return the character of the second item
    return items[1][0]


# ------------------------------------------------------------------
# Example usage
# ------------------------------------------------------------------
if __name__ == "__main__":
    examples = [
        ("aabbc", "b"),          # a:2, b:2, c:1 → a and b tie, a first → second is b
        ("  aa bb cc dd", "b"),  # spaces ignored, a:2, b:2, c:2, d:2 → a first, b second
        ("abc", None),           # only 3 distinct, but all freq 1 → a first, b second → return b
        ("", None),              # no chars
        ("   ", None),           # only spaces
        ("AaaBBB", "B"),         # A:1, a:2, B:3 → B is most, a second
        ("x y z x y", "y"),      # x:2, y:2, z:1 → x first, y second
    ]

    for txt, expected in examples:
        result = second_most_common(txt)
        print(f"second_most_common({txt!r}) → {result!r} (expected {expected!r})")
```

### How it works

1. **Counting** – We use `Counter` to count every non‑space character.
2. **First occurrence** – While iterating over the original string we remember the index of the first time each character appears.
3. **Sorting** – The list of `(char, freq, first_index)` tuples is sorted by:
   * **Frequency** – descending (`-freq`).
   * **First appearance** – ascending (`first_index`).
4. **Result** – The second element of the sorted list is the second most common character. If there are fewer than two distinct characters, we return `None`.

Feel free to drop this function into your project or tweak it to suit any additional constraints!