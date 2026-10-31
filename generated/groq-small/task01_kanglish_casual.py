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
    return s[::-1]          # slice notation: start:end:step (step = -1 reverses)
```

### Quick test

```python
if __name__ == "__main__":
    examples = ["hello", "Python", "12345", ""]
    for txt in examples:
        print(f"{txt!r} -> {reverse_string(txt)!r}")
```

**Output**

```
'hello' -> 'olleh'
'Python' -> 'nohtyP'
'12345' -> '54321'
'' -> ''
```

That’s all you need! The slice `s[::-1]` is the most idiomatic way in Python to reverse a string.