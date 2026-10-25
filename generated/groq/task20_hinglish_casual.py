```python
def compress(s: str) -> str:
    """Compress consecutive repeated characters.

    Example:
        >>> compress("aaabbcaaa")
        'a3b2ca3'
    """
    if not s:
        return ""

    result = []
    count = 1
    prev = s[0]

    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            result.append(prev + (str(count) if count > 1 else ""))
            prev = ch
            count = 1

    # append the last group
    result.append(prev + (str(count) if count > 1 else ""))

    return "".join(result)
```