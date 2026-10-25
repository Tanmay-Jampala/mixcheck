```python
def valid_mobile(s: str) -> bool:
    # Remove all whitespace characters
    s = "".join(s.split())

    # Strip allowed prefixes
    if s.startswith("+91"):
        s = s[3:]
    elif s.startswith("0"):
        s = s[1:]

    # Must be exactly 10 digits and start with 6,7,8,9
    return len(s) == 10 and s.isdigit() and s[0] in "6789"
```