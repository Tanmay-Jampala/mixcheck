**Python – `sort_words`**

```python
from typing import List

def sort_words(sentence: str) -> List[str]:
    """
    Return a list of the unique words in *sentence*.

    * The input sentence contains only alphabetic words separated by a single
      space – no punctuation.
    * Words are treated case‑insensitively; the returned words are all lower‑case.
    * The result is sorted
          1. by increasing length
          2. for equal length, alphabetically.
    * If the sentence is empty (or only whitespace) an empty list is returned.

    Examples
    --------
    >>> sort_words("Apple banana apple Orange")
    ['apple', 'orange', 'banana']

    >>> sort_words("")
    []
    """
    # 1️⃣  Empty / whitespace‑only input → empty list
    if not sentence or sentence.strip() == "":
        return []

    # 2️⃣  Split, normalise to lower‑case and keep only one copy of each word
    #     (using a set gives O(1) look‑up for duplicates)
    unique_words = {word.lower() for word in sentence.split()}

    # 3️⃣  Sort by (length, alphabetical)
    sorted_words = sorted(unique_words, key=lambda w: (len(w), w))

    return sorted_words


# ----------------------------------------------------------------------
# Quick self‑test (run only when the file is executed directly)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ("Apple banana apple Orange", ['apple', 'orange', 'banana']),
        ("dog cat mouse Dog", ['cat', 'dog', 'mouse']),
        ("", []),
        ("One two three Four five six", ['one', 'two', 'six', 'four', 'five', 'three']),
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        result = sort_words(inp)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")
```

### How it works
| Step | What happens | Why |
|------|--------------|-----|
| **1** | `if not sentence or sentence.strip() == "":` | Handles the *empty* case – returns `[]` as required. |
| **2** | `{word.lower() for word in sentence.split()}` | `split()` gives the words (single‑space guaranteed). Converting each to `lower()` makes the function case‑insensitive, and the set removes duplicates. |
| **3** | `sorted(..., key=lambda w: (len(w), w))` | The key is a tuple: first the length (so shorter words come first), then the word itself (alphabetical order for equal lengths). |
| **4** | `return sorted_words` | Returns the final list. |

The function runs in **O(n log n)** time where *n* is the number of distinct words (the sorting step), and uses **O(n)** extra space for the set of unique words.