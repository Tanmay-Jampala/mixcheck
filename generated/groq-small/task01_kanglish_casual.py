Sure!  
Here’s a tiny, clean Python function called **`reverse_string`** that takes a string and returns it reversed.

```python
def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string `s`.

    Parameters
    ----------
    s : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    # The simplest way in Python is to use slicing with a step of -1.
    return s[::-1]


# ---- Example usage ----
if __name__ == "__main__":
    original = "Hello, world!"
    reversed_ = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_}")
```

### How it works
- `s[::-1]` creates a new string that starts at the end of `s` and steps backwards one character at a time, effectively reversing the string.
- The function is type‑annotated (`s: str` → `str`) so static type checkers and IDEs can help you catch mistakes.

Feel free to drop this into your project or tweak it if you need extra features (e.g., handling non‑string inputs, ignoring whitespace, etc.). Happy coding!