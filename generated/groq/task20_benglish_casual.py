```python
def compress(s: str) -> str:
    """
    Compress a string by replacing consecutive repeated characters with
    the character followed by the repeat count.
    If a character appears only once, it is kept as‑is (no count).

    Example:
        compress("aaabbcdddd") -> "a3b2cd4"
    """
    if not s:
        return ""

    result = []
    prev_char = s[0]
    count = 1

    for ch in s[1:]:
        if ch == prev_char:
            count += 1
        else:
            # append previous character and its count (if >1)
            result.append(prev_char + (str(count) if count > 1 else ""))
            prev_char = ch
            count = 1

    # append the last accumulated character
    result.append(prev_char + (str(count) if count > 1 else ""))

    return "".join(result)


# Example usage
if __name__ == "__main__":
    test_cases = [
        "aaabbcdddd",
        "abcd",
        "aabbaa",
        "",
        "zzzzzz",
        "hello world"
    ]

    for t in test_cases:
        print(f"{t!r} -> {compress(t)!r}")
```