Here’s a simple Python function called **`reverse_string`** that takes a string as input and returns the reversed version of that string:

```python
def reverse_string(s: str) -> str:
    """
    Return the reverse of the given string.

    Parameters
    ----------
    s : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.
    """
    # Using Python's slicing syntax to reverse the string
    return s[::-1]


# Example usage
if __name__ == "__main__":
    original = "Hello, world!"
    reversed_str = reverse_string(original)
    print(f"Original : {original}")
    print(f"Reversed : {reversed_str}")
```

**Explanation**

- `s[::-1]` is a slice that steps through the string with a step of `-1`, effectively iterating from the end to the start and producing a new reversed string.
- The function includes type hints (`s: str -> str`) and a docstring for clarity.
- The `if __name__ == "__main__":` block demonstrates how you can call the function and see the result.