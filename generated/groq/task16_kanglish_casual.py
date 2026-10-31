Here’s a compact, pure‑Python implementation that follows the Indian numbering‑system comma placement:

```python
def indian_format(num: int) -> str:
    """
    Return the given non‑negative integer formatted with Indian‑style commas.

    Rules
    -----
    * The last three digits form the first group.
    * All groups to the left of that are two‑digit groups.
    * Numbers smaller than 1 000 are returned unchanged (no commas).

    Parameters
    ----------
    num : int
        A non‑negative integer.  ``ValueError`` is raised for negative values
        or non‑integers.

    Returns
    -------
    str
        The number as a string with commas placed according to the Indian
        convention.

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
    >>> indian_format(1234567)
    '12,34,567'
    >>> indian_format(1234567890)
    '1,23,45,67,890'
    """
    # ---- validation ---------------------------------------------------------
    if not isinstance(num, int):
        raise TypeError("Only integer values are supported.")
    if num < 0:
        raise ValueError("Number must be non‑negative.")

    # ---- numbers < 1 000 need no commas ------------------------------------
    if num < 1000:
        return str(num)

    # ---- work with the decimal representation as a list of characters -------
    s = str(num)
    # split off the last three digits (they always stay together)
    last_three = s[-3:]
    prefix = s[:-3]

    # break the prefix into groups of two, starting from the right
    groups = []
    while len(prefix) > 2:
        groups.append(prefix[-2:])   # take the right‑most two digits
        prefix = prefix[:-2]        # shrink the prefix
    # whatever is left (1 or 2 digits) becomes the left‑most group
    if prefix:
        groups.append(prefix)

    # groups were collected from right to left → reverse them
    groups = groups[::-1]

    # join everything with commas
    return ','.join(groups + [last_three])
```

### How it works
1. **Validation** – ensures the input is a non‑negative integer.
2. **Small numbers** – if the value is `< 1000` we simply return it unchanged.
3. **String slicing** – the last three digits are kept together (`last_three`).
4. **Two‑digit grouping** – the remaining left‑hand part (`prefix`) is sliced into
   two‑digit chunks from right to left, stored in `groups`, then reversed to get
   the correct order.
5. **Join** – all groups (including the final three‑digit group) are concatenated
   with commas.

You can drop this function into any script or module and call it directly:

```python
print(indian_format(123456789))   # → 12,34,56,789
print(indian_format(1000))        # → 1,000
print(indian_format(999))         # → 999
```

Feel free to adapt it for floats (e.g., split on the decimal point first) if you need that extra functionality.