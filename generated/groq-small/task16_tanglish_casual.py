```python
def indian_format(n: int) -> str:
    """
    Return a string representation of a non‑negative integer `n`
    formatted with Indian style commas.
    
    Example:
        indian_format(123456789) -> '12,34,56,789'
        indian_format(1234)      -> '1,234'
        indian_format(999)       -> '999'
    """
    if n < 0:
        raise ValueError("Only non‑negative numbers are supported")

    s = str(n)
    if len(s) <= 3:
        return s

    # Reverse the string to process from least significant digit
    rev = s[::-1]
    parts = []

    # First group of 3 digits
    parts.append(rev[:3])

    # Remaining groups of 2 digits
    i = 3
    while i < len(rev):
        parts.append(rev[i:i+2])
        i += 2

    # Join with commas and reverse back
    return ','.join(part[::-1] for part in parts[::-1])
```