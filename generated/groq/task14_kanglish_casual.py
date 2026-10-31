**Python function – `are_anagrams`**

```python
def are_anagrams(word1: str, word2: str) -> bool:
    """
    Return True if `word1` and `word2` are anagrams of each other.
    Both arguments must be lowercase alphabetic strings.
    """
    # Quick length check – if lengths differ they cannot be anagrams
    if len(word1) != len(word2):
        return False

    # Count the occurrences of each character in both words
    # Using `collections.Counter` is concise and O(n)
    from collections import Counter
    return Counter(word1) == Counter(word2)
```

### ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?

1. **ಲಂಬೈ (length) ಪರಿಶೀಲನೆ** – ಎರಡು ಪದಗಳ ಉದ್ದ ಒಂದೇ ಇಲ್ಲದಿದ್ದರೆ, ತಕ್ಷಣ `False` ಹಿಂತಿರುಗುತ್ತದೆ.  
2. **ಅಕ್ಷರಗಳ ಎಣಿಕೆ** – `collections.Counter` ಪ್ರತಿ ಅಕ್ಷರ ಎಷ್ಟು ಬಾರಿ ಬರುತ್ತದೆ ಎಂಬುದನ್ನು ಡಿಕ್ಷನರಿ‑ರೀತಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.  
3. **ಸಮಾನತೆ ಹೋಲಿಕೆ** – ಎರಡೂ ಕೌಂಟರ್‌ಗಳು ಒಂದೇ ಆಗಿದ್ದರೆ, ಅಂದರೆ ಪ್ರತಿ ಅಕ್ಷರವೂ ಒಂದೇ ಸಂಖ್ಯೆಯಲ್ಲಿ ಇದೆ → `True`; ಇಲ್ಲದಿದ್ದರೆ `False`.

### ಉದಾಹರಣೆ ಬಳಕೆ

```python
print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "papel"))    # True
print(are_anagrams("hello", "world"))    # False
print(are_anagrams("abc", "ab"))         # False   (ಉದ್ದ ಬೇರೆ)
```

> **ಗಮನಿಸಿ:** ಈ ಫಂಕ್ಷನ್ ಇನ್‌ಪುಟ್‌ಗಳು ಕೇವಲ ಇಂಗ್ಲೀಷ್ ಅಕ್ಷರಗಳ (a‑z) ಚಿಕ್ಕ ಅಕ್ಷರಗಳೇ ಎಂದು ಊಹಿಸುತ್ತದೆ. ಬೇರೆ ಅಕ್ಷರಗಳು, ಖಾಲಿ ಜಾಗ, ಅಥವಾ ವಿಶೇಷ ಚಿಹ್ನೆಗಳು ಇದ್ದರೆ, ಅವುಗಳನ್ನು ಮೊದಲೇ ಸ್ವಚ್ಛಗೊಳಿಸಬೇಕು.