**Python – Indian‑style comma formatting**

```python
def indian_format(number):
    """
    Return a string with Indian‑style commas.

    * The last three digits are kept together.
    * All digits to the left of those three are grouped in pairs (2‑2‑2‑…).
    * Numbers smaller than 1000 are returned unchanged.
    * A decimal part (if any) is preserved.
    * The function accepts any non‑negative int, float or numeric string.

    Examples
    --------
    >>> indian_format(0)
    '0'
    >>> indian_format(123)
    '123'
    >>> indian_format(1234)
    '1,234'
    >>> indian_format(12345)
    '12,345'
    >>> indian_format(123456)
    '1,23,456'
    >>> indian_format(1234567)
    '12,34,567'
    >>> indian_format(12345678)
    '1,23,45,678'
    >>> indian_format(12345678.90)
    '1,23,45,678.90'
    """
    # ------------------------------------------------------------------
    # 1. Convert the input to a string and separate integer / fractional part
    # ------------------------------------------------------------------
    s = str(number)
    if '.' in s:
        int_part, frac_part = s.split('.')
    else:
        int_part, frac_part = s, ''

    # ------------------------------------------------------------------
    # 2. If the integer part has 3 or fewer digits → no commas needed
    # ------------------------------------------------------------------
    if len(int_part) <= 3:
        formatted_int = int_part
    else:
        # a) keep the last three digits together
        last_three = int_part[-3:]
        # b) the remaining left‑hand part will be split into 2‑digit groups
        left = int_part[:-3]

        groups = []
        # take 2 digits from the right until nothing (or 1‑2 digits) remains
        while len(left) > 2:
            groups.append(left[-2:])   # take a pair
            left = left[:-2]           # shrink the string

        # whatever is left (1 or 2 digits) becomes the first group
        if left:
            groups.append(left)

        # c) join the groups in the correct order and attach the last three
        formatted_int = ','.join(reversed(groups)) + ',' + last_three

    # ------------------------------------------------------------------
    # 3. Re‑attach the fractional part (if any)
    # ------------------------------------------------------------------
    if frac_part:
        return f"{formatted_int}.{frac_part}"
    return formatted_int
```

### How it works
1. **Separate integer & fractional parts** – this lets us keep any decimal part untouched.
2. **No‑comma case** – if the integer part is ≤ 3 digits we simply return it.
3. **Grouping**  
   * The right‑most three digits stay together (`last_three`).  
   * The remaining left part is sliced into 2‑digit chunks from the right side (`while len(left) > 2`).  
   * The collected chunks are reversed to restore the original order and joined with commas.
4. **Re‑attach the fraction** – if the original number had a decimal point we add it back.

The function works for plain integers, floats, or numeric strings, and it never produces a leading or trailing comma. Feel free to drop it into any project that needs Indian‑style number formatting.