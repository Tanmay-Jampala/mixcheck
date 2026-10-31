Below is a compact, well‑documented implementation of the “run‑length” compressor you described.  
It keeps a single character as‑is, but appends the count when the same character appears more than once consecutively.

```python
def compress_string(s: str) -> str:
    """
    Compress a string by collapsing consecutive identical characters.

    Parameters
    ----------
    s : str
        The input string to compress.

    Returns
    -------
    str
        The compressed representation:
        * a single character is kept unchanged,
        * a run of N identical characters (N > 1) becomes `char + str(N)`.

    Examples
    --------
    >>> compress_string('aaabbc')
    'a3b2c'
    >>> compress_string('abcd')
    'abcd'
    >>> compress_string('')
    ''
    >>> compress_string('a')
    'a'
    >>> compress_string('aabbaa')
    'a2b2a2'
    """
    if not s:                     # Fast‑path for empty input
        return ''

    result = []                    # Use a list for efficient string concatenation
    current_char = s[0]
    count = 1

    for ch in s[1:]:
        if ch == current_char:
            count += 1
        else:
            # Append the current run
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            # Reset for the next run
            current_char = ch
            count = 1

    # Append the final run
    result.append(current_char)
    if count > 1:
        result.append(str(count))

    return ''.join(result)
```

### How it works

1. **Edge cases** – If the input is empty, we return an empty string immediately.
2. **Iteration** – We walk through the string once, keeping track of the current character and how many times it has appeared consecutively (`count`).
3. **Run boundary** – When the next character differs, we flush the current run to the result list:
   * Append the character itself.
   * Append the count *only* if it is greater than 1.
4. **Final run** – After the loop, we flush the last run in the same way.
5. **Return** – Join the list into a single string.

### Alternative: using `itertools.groupby`

If you prefer a more declarative style, the same logic can be expressed with `groupby`:

```python
from itertools import groupby

def compress_string_groupby(s: str) -> str:
    return ''.join(
        f'{char}{len(list(group)) if len(list(group)) > 1 else ""}'
        for char, group in groupby(s)
    )
```

Both versions run in **O(n)** time and use **O(1)** additional space (apart from the output string).  
Feel free to drop the function into your project and tweak it (e.g., add error handling, support for Unicode, etc.) as needed.