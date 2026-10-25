Here’s a simple Python function called **`count_vowels`** that receives a string, counts how many vowels ( `a, e, i, o, u` — both lower‑case and upper‑case) it contains, and returns that count.

```python
def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the given string.
    Both lower‑case and upper‑case vowels are counted.

    Parameters
    ----------
    s : str
        The input string to be examined.

    Returns
    -------
    int
        The total count of vowels found in `s`.
    """
    # A set gives O(1) lookup time for each character
    vowels = set('aeiouAEIOU')
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count


# -------------------------------------------------
# Example usage
if __name__ == "__main__":
    test_strings = [
        "Hello World!",          # 3 vowels (e, o, o)
        "Python",                # 1 vowel  (o)
        "AEIOU aeiou",           # 10 vowels (all of them)
        "12345!@#$%",            # 0 vowels
        "",                      # 0 vowels
    ]

    for txt in test_strings:
        print(f"'{txt}' -> {count_vowels(txt)} vowel(s)")
```

### How it works
1. **`vowels` set** – contains all six vowel characters we care about (`a, e, i, o, u` in both cases). Using a set makes the membership test (`ch in vowels`) fast.
2. **Loop through the string** – for each character `ch` we check if it’s in the `vowels` set; if so, we increment `count`.
3. **Return the total** – after scanning the whole string, the function returns the accumulated count.

Feel free to copy‑paste the function into your own project, or adapt the set if you ever need to include additional vowel characters (e.g., accented vowels).