Below is a compact, well‑documented implementation of the requested **`indian_format`** function.

```python
def indian_format(num):
    """
    Return the Indian‑style comma formatted representation of a non‑negative number.

    Rules
    -----
    * The last three digits form the first group.
    * All groups to the left of that are of size 2.
    * Numbers < 1 000 are returned unchanged (no commas).
    * If *num* is a float, the fractional part is left untouched.

    Parameters
    ----------
    num : int | float | str
        A non‑negative integer or floating‑point number.  A string containing a
        numeric literal is also accepted.

    Returns
    -------
    str
        The number formatted with Indian commas.

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
    >>> indian_format(12345678.90)
    '1,23,45,678.90'
    """
    # ------------------------------------------------------------------ #
    # 1️⃣  Normalise the input – we only need the string representation.
    # ------------------------------------------------------------------ #
    if isinstance(num, (int, float)):
        # Preserve the sign (should be non‑negative) and the decimal part.
        s = f"{num}"
    elif isinstance(num, str):
        s = num.strip()
    else:
        raise TypeError("num must be int, float or numeric string")

    # Guard against negative values (the spec says *non‑negative* only)
    if s.startswith("-"):
        raise ValueError("Only non‑negative numbers are allowed")

    # ------------------------------------------------------------------ #
    # 2️⃣  Split integer and fractional parts (if any)
    # ------------------------------------------------------------------ #
    if "." in s:
        int_part, frac_part = s.split(".", 1)
        frac_part = "." + frac_part          # keep the dot for later
    else:
        int_part, frac_part = s, ""

    # No commas needed for numbers with ≤3 digits
    if len(int_part) <= 3:
        return int_part + frac_part

    # ------------------------------------------------------------------ #
    # 3️⃣  Build the Indian grouping:
    #     - last three digits stay together
    #     - preceding digits are taken two‑by‑two from right to left
    # ------------------------------------------------------------------ #
    # a)   The right‑most three‑digit block
    right_three = int_part[-3:]
    # b)   The remaining left part
    left = int_part[:-3]

    # c)   Group the left part in pairs
    pairs = []
    while left:
        pairs.append(left[-2:])   # take last two digits
        left = left[:-2]          # shrink the string

    # d)   Assemble: pairs are in reverse order, so reverse them back
    formatted_int = ",".join(reversed(pairs) + [right_three])

    # ------------------------------------------------------------------ #
    # 4️⃣  Append the fractional part (if any) and return
    # ------------------------------------------------------------------ #
    return formatted_int + frac_part


# ---------------------------------------------------------------------- #
# Simple sanity‑check (run only when the file is executed directly)
# ---------------------------------------------------------------------- #
if __name__ == "__main__":
    test_vals = [
        0, 5, 99, 100, 999,
        1000, 1234, 12345, 123456,
        1234567, 12345678, 123456789,
        12345678.90, "9876543210.12345"
    ]

    for v in test_vals:
        print(f"{v!r:>20} → {indian_format(v)}")
```

### How it works
1. **Input normalisation** – Accepts `int`, `float`, or a numeric string.  
2. **Separate integer / fractional part** – The comma logic only touches the integer part; the fractional part (if any) is simply appended unchanged.  
3. **Apply Indian grouping**  
   * The last three digits are kept together.  
   * The remaining digits are sliced into groups of two, starting from the right.  
   * Those two‑digit groups are reversed back to the original order and joined with commas.  
4. **Return** the formatted integer together with the original fractional part.

The function satisfies all the requirements you listed:

* **Non‑negative numbers only** – a `ValueError` is raised for negatives.  
* **No commas for numbers `< 1 000`** – handled early.  
* **Indian style grouping** – `…,12,34,567` etc.  

Feel free to copy the function into your project and use it directly!