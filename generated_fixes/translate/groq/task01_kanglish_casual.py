Here’s a concise implementation of `reverse_string` in Python:

```python
def reverse_string(s: str) -> str:
    """
    Return a new string that is the reverse of the input string `s`.

    Parameters
    ----------
    s : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.

    Examples
    --------
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("")
    ''
    """
    # The simplest way is to use Python's slicing syntax with a step of -1
    return s[::-1]


# ---- Simple test cases ----
if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("", ""),
        ("a", "a"),
        ("racecar", "racecar"),
    ]

    for inp, expected in test_cases:
        result = reverse_string(inp)
        assert result == expected, f"Failed for input {inp!r}: expected {expected!r}, got {result!r}"
    print("All tests passed!")
```

**Explanation**

- `s[::-1]` uses Python’s slice notation: start at the end of the string and step backwards by 1, effectively reversing the sequence.
- The function includes type hints (`s: str -> str`) and a docstring that explains its behavior and provides usage examples.
- A small test harness under `if __name__ == "__main__":` runs a few assertions to verify correctness.