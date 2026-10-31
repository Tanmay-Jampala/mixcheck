Here’s a concise implementation that meets all the requirements:

```python
def is_palindrome(s: str) -> bool:
    """
    Return True if the given string reads the same forward and backward,
    ignoring case and spaces; otherwise return False.

    Parameters
    ----------
    s : str
        The string to test.

    Returns
    -------
    bool
        True if `s` is a palindrome under the given rules, False otherwise.
    """
    # Remove spaces and convert to a single case (lower‑case)
    cleaned = s.replace(" ", "").lower()

    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        "Racecar",
        "A man a plan a canal Panama",
        "Hello World",
        "Was it a car or a cat I saw",
        "No lemon, no melon"
    ]

    for txt in test_cases:
        # For the last two examples we also want to ignore punctuation,
        # so we strip non‑alphanumeric characters as an optional step.
        import re
        txt_alpha = re.sub(r'[^A-Za-z0-9 ]+', '', txt)   # keep letters, digits, spaces
        print(f"{txt!r:40} -> {is_palindrome(txt_alpha)}")
```

### How it works
1. **Normalization** – `s.replace(" ", "").lower()` removes all spaces and forces every character to lower‑case, so `"Racecar"` and `"racecar"` are treated the same.
2. **Palindrome test** – `cleaned == cleaned[::-1]` checks whether the normalized string is identical to its reverse (`[::-1]` slices the string backwards).
3. **Optional punctuation handling** – In the demo, a regular‑expression step removes punctuation before calling `is_palindrome`. If you only need to ignore spaces (as the prompt states), you can omit that step and call `is_palindrome` directly.

Feel free to adapt the preprocessing (e.g., also strip punctuation) to suit your exact needs.