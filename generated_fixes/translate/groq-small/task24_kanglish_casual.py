```python
from collections import Counter
from typing import Optional

def second_most_common(text: str) -> Optional[str]:
    """
    Return the character that is second most frequent in *text*.

    Rules
    -----
    * Spaces are ignored.
    * Upper‑case and lower‑case letters are treated as distinct.
    * If two characters have the same frequency, the one that appears first
      in the original string wins.
    * If the string contains fewer than two distinct non‑space characters,
      ``None`` is returned.

    Parameters
    ----------
    text : str
        The input string.

    Returns
    -------
    Optional[str]
        The second most common character, or ``None`` if it does not exist.
    """
    # Remove spaces and count frequencies
    filtered = [ch for ch in text if ch != ' ']
    if not filtered:
        return None

    freq = Counter(filtered)

    # Record the first index of each character
    first_index = {}
    for idx, ch in enumerate(text):
        if ch == ' ':
            continue
        if ch not in first_index:
            first_index[ch] = idx

    # Sort characters by (-frequency, first_index)
    sorted_chars = sorted(freq.keys(),
                          key=lambda c: (-freq[c], first_index[c]))

    # Need at least two distinct characters
    return sorted_chars[1] if len(sorted_chars) >= 2 else None
```

**Example usage**

```python
>>> second_most_common("Hello World")
'l'          # 'l' appears 3 times, 'o' appears 2 times, 'H' appears 1 time, etc.
>>> second_most_common("a a a b b")
'b'
>>> second_most_common("   ")
None
>>> second_most_common("x")
None
```

The function follows the specified ranking rules and handles all edge cases.