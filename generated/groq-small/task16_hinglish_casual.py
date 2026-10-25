```python
def indian_format(num):
    """
    Format a non‑negative number using Indian comma convention.
    Example:
        1234567 -> "12,34,567"
        1234    -> "1,234"
        999     -> "999"
    Supports integers and floats (fractional part is preserved).
    """
    if num < 0:
        raise ValueError("Number must be non‑negative")

    # Convert to string and split integer/fractional parts
    s = str(num)
    if '.' in s:
        int_part, frac_part = s.split('.', 1)
    else:
        int_part, frac_part = s, None

    # Reverse the integer part to process from least significant digit
    rev = int_part[::-1]
    groups = [rev[:3]]          # first group of 3 digits
    rev = rev[3:]

    # Subsequent groups of 2 digits
    while rev:
        groups.append(rev[:2])
        rev = rev[2:]

    # Join groups with commas and reverse back
    formatted_int = ','.join(g[::-1] for g in groups[::-1])

    # Append fractional part if present
    if frac_part is not None:
        formatted_int += '.' + frac_part

    return formatted_int
```