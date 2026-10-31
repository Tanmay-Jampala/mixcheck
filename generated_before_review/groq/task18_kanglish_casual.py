**Python function – `sort_words`**

```python
from typing import List

def sort_words(sentence: str) -> List[str]:
    """
    Return a list of the unique words in *sentence* (all lower‑cased),
    sorted first by length (shortest → longest) and then alphabetically
    for words of the same length.

    Rules
    -----
    * The input sentence contains only words separated by a single space,
      no punctuation.
    * Words that differ only by case (e.g. "Apple" and "apple") are treated
      as the same word – the lower‑cased form is kept.
    * If the sentence is empty (or only whitespace) an empty list is returned.

    Parameters
    ----------
    sentence: str
        A space‑separated string of words.

    Returns
    -------
    List[str]
        Sorted list of unique, lower‑cased words.

    Examples
    --------
    >>> sort_words("Banana apple Orange banana")
    ['apple', 'banana', 'orange']

    >>> sort_words("")
    []

    >>> sort_words("cat dog ant bee")
    ['ant', 'bee', 'cat', 'dog']
    """
    # 1️⃣  Empty or whitespace‑only input → empty list
    if not sentence or sentence.strip() == "":
        return []

    # 2️⃣  Split, lower‑case and deduplicate
    #     Using a set guarantees uniqueness irrespective of original case.
    unique_words = {word.lower() for word in sentence.split()}

    # 3️⃣  Sort by (length, alphabetical)
    sorted_words = sorted(unique_words, key=lambda w: (len(w), w))

    return sorted_words


# ----------------------------------------------------------------------
# Quick self‑test (run only when this file is executed directly)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ("Banana apple Orange banana", ['apple', 'banana', 'orange']),
        ("cat dog ant bee", ['ant', 'bee', 'cat', 'dog']),
        ("", []),
        ("  ", []),
        ("Hello hello HELLO world WORLD", ['world', 'hello']),
        ("a aa aaa aaaa", ['a', 'aa', 'aaa', 'aaaa']),
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        result = sort_words(inp)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    print("All tests passed!")
```

### How it works
1. **Empty check** – If the string is empty or only spaces, we immediately return `[]`.
2. **Normalization & deduplication** –  
   ```python
   {word.lower() for word in sentence.split()}
   ```  
   splits on the single spaces, lower‑cases each token, and stores them in a set, automatically removing duplicates (including those that differ only by case).
3. **Sorting** – `sorted(..., key=lambda w: (len(w), w))` orders the words by:
   * `len(w)` – shortest first,
   * `w` – alphabetical order when lengths are equal.
4. **Return** – The sorted list is returned.

Feel free to drop this function into any module or script; it meets all the requirements you described.