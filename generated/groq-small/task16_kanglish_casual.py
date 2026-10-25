**Python – Indian‑style number formatter**

```python
def indian_format(n: int) -> str:
    """
    Return a string representation of a non‑negative integer `n`
    formatted with Indian‑style commas.

    Indian grouping rules:
        • The last three digits form the first group.
        • All preceding digits are grouped in pairs (2‑digit groups).
        • Numbers < 1000 are returned unchanged (no comma).

    Parameters
    ----------
    n : int
        Non‑negative integer to format.

    Returns
    -------
    str
        The formatted number.

    Raises
    ------
    ValueError
        If `n` is negative.

    Examples
    --------
    >>> indian_format(0)
    '0'
    >>> indian_format(999)
    '999'
    >>> indian_format(1000)
    '1,000'
    >>> indian_format(12345)
    '12,345'
    >>> indian_format(123456)
    '1,23,456'
    >>> indian_format(1234567)
    '12,34,567'
    >>> indian_format(123456789)
    '12,34,56,789'
    """
    if n < 0:
        raise ValueError("Only non‑negative numbers are allowed")

    s = str(n)

    # No comma needed for numbers with 3 or fewer digits
    if len(s) <= 3:
        return s

    # Split into the last 3 digits and the remaining part
    last3 = s[-3:]
    rest = s[:-3]

    # Group the remaining part in pairs from the right
    rev_rest = rest[::-1]                     # reverse for easy chunking
    pairs = [rev_rest[i:i + 2] for i in range(0, len(rev_rest), 2)]

    # Reverse each pair back and join with commas
    grouped_rest = ','.join(pair[::-1] for pair in pairs[::-1])

    return f"{grouped_rest},{last3}"
```

### How it works

1. **Short numbers** – If the number has 3 or fewer digits, it is returned as‑is.
2. **Last three digits** – These are kept as the final group.
3. **Remaining digits** – Reversed, split into 2‑digit chunks, then reversed back.
4. **Join** – The 2‑digit groups are joined with commas, followed by the last‑3‑digit group.

Feel free to copy‑paste the function into your project. It works for any non‑negative integer; if you need to support floats, split the integer and fractional parts separately and apply the same logic to the integer part.