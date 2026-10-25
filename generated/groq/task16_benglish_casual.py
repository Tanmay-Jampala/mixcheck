```python
def indian_format(num):
    """
    Return the Indian‑style comma formatted string for a non‑negative integer.
    Numbers < 1000 are returned without commas.
    """
    # Ensure we are working with an integer part only
    n = int(num)
    if n < 1000:
        return str(n)

    s = str(n)[::-1]          # reverse the string for easy grouping
    groups = [s[:3]]          # first group of three digits
    s = s[3:]

    while s:                  # subsequent groups of two digits
        groups.append(s[:2])
        s = s[2:]

    # Join groups with commas, reverse each group back, then reverse whole string
    return ','.join(g[::-1] for g in groups)[::-1]
```