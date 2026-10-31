**Python‑ನಲ್ಲಿ “compress” ಫಂಕ್ಷನ್ (ಒಂದೇ ಅಕ್ಷರಗಳು ಪುನರಾವರ್ತಿಸಿದರೆ ಅಕ್ಷರ + ಎಷ್ಟು ಸಲ ಎಂದು, ಒಂದೇ ಸಲ ಬಂದರೆ ಅಕ್ಷರ ಮಾತ್ರ)**

```python
def compress(s: str) -> str:
    """
    ಕೊಟ್ಟಿರುವ ಸ್ಟ್ರಿಂಗ್ s ಅನ್ನು ಸಂಕುಚಿತಗೊಳಿಸಿ.

    - ಒಂದೇ ಅಕ್ಷರವು ನಿರಂತರವಾಗಿ ಪುನರಾವರ್ತಿಸಿದರೆ:  ಅಕ್ಷರ + ಪುನರಾವರ್ತನೆಯ ಸಂಖ್ಯೆ
    - ಅಕ್ಷರವು ಒಂದೇ ಸಲ ಬಂದರೆ:  ಅಕ್ಷರ ಮಾತ್ರ (ಸಂಖ್ಯೆ ಬರೆಯುವುದಿಲ್ಲ)

    ಉದಾಹರಣೆ:
        compress('aaabbc')  ->  'a3b2c'
        compress('abc')     ->  'abc'
    """
    if not s:                     # ಖಾಲಿ ಸ್ಟ್ರಿಂಗ್
        return ""

    result = []                   # ಫಲಿತಾಂಶವನ್ನು ಪಟ್ಟಿಯಾಗಿ ಸಂಗ್ರಹಿಸಿ
    count = 1                     # ಪ್ರಸ್ತುತ ಅಕ್ಷರದ ಎಣಿಕೆ

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:      # ಅದೇ ಅಕ್ಷರ ಮುಂದುವರಿದರೆ ಎಣಿಕೆ ಹೆಚ್ಚಿಸಿ
            count += 1
        else:                     # ಅಕ್ಷರ ಬದಲಾಗಿದೆ
            result.append(s[i - 1])          # ಹಿಂದಿನ ಅಕ್ಷರ ಸೇರಿಸಿ
            if count > 1:                    # 1 ಕ್ಕಿಂತ ಹೆಚ್ಚು ಇದ್ದರೆ ಸಂಖ್ಯೆ ಸೇರಿಸಿ
                result.append(str(count))
            count = 1                         # ಎಣಿಕೆಯನ್ನು ಮರುಹೊಂದಿಸಿ

    # ಕೊನೆಯ ಗುಂಪು
    result.append(s[-1])
    if count > 1:
        result.append(str(count))

    return ''.join(result)
```

---

### `itertools.groupby` ಬಳಸಿ ಇನ್ನೂ ಸಂಕ್ಷಿಪ್ತವಾಗಿ

```python
from itertools import groupby

def compress(s: str) -> str:
    return ''.join(
        f"{ch}{len(list(g))}" if len(list(g)) > 1 else ch
        for ch, g in groupby(s)
    )
```

> **ಗಮನಿಸಿ**  
> - `groupby` ಬಳಸುವಾಗ `list(g)` ಅನ್ನು ಎರಡು ಬಾರಿ ಬಳಸುವ ಕಾರಣದಿಂದ, ದೊಡ್ಡ ಸ್ಟ್ರಿಂಗ್‌ಗಳಿಗಾಗಿ ಇದು ಸ್ವಲ್ಪ ನಿಧಾನವಾಗಬಹುದು.  
> - ಮೊದಲ ವಿಧಾನವು O(n) ಸಮಯ ಮತ್ತು O(1) ಹೆಚ್ಚುವರಿ ಸ್ಥಳ (ಫಲಿತಾಂಶ ಹೊರತುಪಡಿಸಿ) ಬಳಸುತ್ತದೆ.

---

### ಪರೀಕ್ಷೆ

```python
tests = [
    ("aaabbc", "a3b2c"),
    ("abc", "abc"),
    ("", ""),
    ("a", "a"),
    ("zzzzzz", "z6"),
    ("aabbaa", "a2b2a2")
]

for inp, expected in tests:
    out = compress(inp)
    print(inp, "->", out, "|", "PASS" if out == expected else "FAIL")
```

ಎಲ್ಲಾ ಪರೀಕ್ಷೆಗಳು “PASS” ಆಗಿರಬೇಕು.  

ಇದು ನಿಮ್ಮ ಅಗತ್ಯಕ್ಕೆ ಸರಿಹೊಂದುತ್ತದೆ ಎಂದು ಭಾವಿಸುತ್ತೇನೆ!