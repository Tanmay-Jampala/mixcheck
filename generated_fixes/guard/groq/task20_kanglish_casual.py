```python
def compress(s: str) -> str:
    """
    Run‑length encode the input string.

    For each group of consecutive identical characters:
        - If the group length is 1 → output the character.
        (e.g., "a")
        - If the group length > 1 → output the character followed by the count.
        (e.g., "a5")

    Parameters
    ----------
    s: str
        Input string to compress.

    Returns
    -------
    str
        The compressed representation.
    """
    if not s:
        return ""

    result = []
    prev = s[0]
    count = 1

    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            # flush previous run
            result.append(prev if count == 1 else f"{prev}{count}")
            prev = ch
            count = 1

    # flush the final run
    result.append(prev if count == 1 else f"{prev}{count}")

    return "".join(result)
```