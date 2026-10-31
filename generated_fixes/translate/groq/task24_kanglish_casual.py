**Python implementation**

```python
def second_most_common(s: str):
    """
    Return the character that ranks second in frequency in *s*.

    Rules
    -----
    * Spaces are ignored.
    * Upper‑ and lower‑case letters are treated as different characters.
    * Characters are first ordered by descending frequency.
    * When two (or more) characters have the same frequency the one that
      appears earlier in the original string comes first.
    * If the string contains fewer than two distinct (non‑space) characters,
      ``None`` is returned.

    Parameters
    ----------
    s: str
        Input string.

    Returns
    -------
    str | None
        The character in the second position of the ranking, or ``None``.
    """
    # ------------------------------------------------------------------
    # 1️⃣  Count frequencies while remembering the first index of each char.
    # ------------------------------------------------------------------
    freq = {}          # char -> count
    first_idx = {}     # char -> first position (ignoring spaces)

    for i, ch in enumerate(s):
        if ch == " ":
            continue                     # ignore spaces
        freq[ch] = freq.get(ch, 0) + 1
        if ch not in first_idx:          # store only the first occurrence
            first_idx[ch] = i

    # ------------------------------------------------------------------
    # 2️⃣  If we have fewer than two distinct characters, we are done.
    # ------------------------------------------------------------------
    if len(freq) < 2:
        return None

    # ------------------------------------------------------------------
    # 3️⃣  Sort by:
    #       • descending frequency  (‑freq)
    #       • ascending first index (first appearance)
    # ------------------------------------------------------------------
    sorted_items = sorted(
        freq.items(),
        key=lambda kv: (-kv[1], first_idx[kv[0]])
    )

    # ------------------------------------------------------------------
    # 4️⃣  Return the character that ends up in position 2 (index 1).
    # ------------------------------------------------------------------
    return sorted_items[1][0]


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    examples = [
        "abcaab",          # a:3, b:2, c:1  → second most common = 'b'
        "aAaA",            # a:2, A:2 (tie → first occurrence decides) → second = 'A'
        "   ",             # no non‑space chars → None
        "x",               # only one distinct char → None
        "ab bc cd de",     # a:1,b:2,c:2,d:2,e:1 → frequencies tie,
                           # first occurrences: b (idx1), c (idx3), d (idx5)
                           # → ranking: b, c, d, a, e → second = 'c'
    ]

    for txt in examples:
        print(f"{txt!r:15} → {second_most_common(txt)!r}")
```

**Explanation of the algorithm**

1. **Counting & first‑occurrence tracking** –  
   While scanning the string once (`O(n)`), we skip spaces, increment a frequency
   dictionary, and store the index of the first time each character appears.

2. **Sorting** –  
   The dictionary items are sorted with a custom key:
   * `-freq` makes the sort descending by count.
   * `first_idx[char]` resolves ties by the earliest appearance in the original
     string.

   The sort runs in `O(k log k)` where `k` is the number of distinct characters
   (at most 256 for ASCII, far smaller than the length of the input).

3. **Result extraction** –  
   If there are at least two distinct characters, the character at index 1 of the
   sorted list is returned; otherwise `None` is returned.

The function satisfies all the requirements: spaces ignored, case‑sensitive,
ties broken by first occurrence, and a graceful `None` when a second most
common character does not exist.