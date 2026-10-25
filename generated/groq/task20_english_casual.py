```python
def compress(s: str) -> str:
    """Compress a string by collapsing consecutive identical characters.

    Each run of a character is replaced by the character followed by the
    count of repetitions, except when the count is 1 (the count is omitted).

    Example:
        compress("aaabbcaaa") -> "a3b2ca3"
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
            result.append(prev + (str(count) if count > 1 else ""))
            prev = ch
            count = 1

    # append the final run
    result.append(prev + (str(count) if count > 1 else ""))

    return "".join(result)
```