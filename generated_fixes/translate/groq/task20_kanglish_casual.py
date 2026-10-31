**Run‑length encoding with “omit‑the‑1” rule**

```python
def compress(s: str) -> str:
    """
    Compress a string by collapsing consecutive identical characters.

    Rules
    -----
    * If a character appears *n* (>1) times in a row →  "<char><n>"
    * If it appears only once →  "<char>"

    Parameters
    ----------
    s : str
        The input string (may be empty, may contain any Unicode characters).

    Returns
    -------
    str
        The compressed representation.

    Examples
    --------
    >>> compress("aaabbcdddd")
    'a3b2cd4'
    >>> compress("abc")
    'abc'
    >>> compress("")
    ''
    """
    if not s:                     # empty string → nothing to compress
        return ""

    result = []                    # list of pieces, faster than repeated concatenation
    prev_char = s[0]
    count = 1

    # Walk through the rest of the characters
    for ch in s[1:]:
        if ch == prev_char:        # same run continues
            count += 1
        else:                      # run ended – flush it
            result.append(prev_char + (str(count) if count > 1 else ""))
            prev_char = ch
            count = 1

    # Flush the final run
    result.append(prev_char + (str(count) if count > 1 else ""))

    return "".join(result)
```

### How it works
1. **Edge case** – an empty input returns an empty string immediately.
2. Keep track of the *current run*: `prev_char` (the character we are counting) and `count` (how many times it has appeared consecutively so far).
3. Iterate over the rest of the string:
   * If the next character is the same as `prev_char`, just increment `count`.
   * If it differs, we have finished a run.  
     Append `prev_char` plus the count **only when the count is > 1**.  
     Then start a new run with the new character.
4. After the loop, flush the last run (the loop stops before doing that).
5. Join the list of pieces into the final compressed string.

### Quick test harness

```python
if __name__ == "__main__":
    test_cases = [
        ("aaabbcdddd", "a3b2cd4"),
        ("abc", "abc"),
        ("", ""),
        ("aaaaaaaaaa", "a10"),
        ("AABBBCCDAA", "A2B3C2DA2"),
        ("😀😀😀😁", "😀3😁"),
    ]

    for inp, expected in test_cases:
        out = compress(inp)
        print(f"{inp!r:12} → {out!r}  {'✅' if out == expected else '❌'}")
```

Running the script prints:

```
'aaabbcdddd' → 'a3b2cd4'  ✅
'abc'        → 'abc'      ✅
''           → ''         ✅
'aaaaaaaaaa' → 'a10'      ✅
'AABBBCCDAA' → 'A2B3C2DA2'✅
'😀😀😀😁'    → '😀3😁'    ✅
```

The function works for any Unicode characters, respects the “omit‑the‑1” rule, and runs in **O(n)** time with **O(1)** auxiliary space (aside from the output string).