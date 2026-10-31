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
    # Using slicing to reverse the string
    return s[::-1]


# Example usage
if __name__ == "__main__":
    original = "Hello, world!"
    reversed_str = reverse_string(original)
    print(f"Original : {original}")
    print(f"Reversed : {reversed_str}")
```

**Explanation**

- `s[::-1]` is a Python slicing idiom that steps through the string `s` backwards, effectively reversing it.
- The function includes type hints (`s: str -> str`) and a docstring for clarity.
- The `if __name__ == "__main__":` block demonstrates how you might call the function and see the result.