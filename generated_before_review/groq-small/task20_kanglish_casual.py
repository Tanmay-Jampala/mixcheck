**Python‑ನಲ್ಲಿ “Run‑Length Encoding” (RLE) – ಒಂದು ಸರಳ ಸಂಕ್ಷಿಪ್ತ ಫಂಕ್ಷನ್**

```python
def compress(s: str) -> str:
    """
    ಕೊಟ್ಟಿರುವ ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ಸಂಕ್ಷಿಪ್ತಗೊಳಿಸುತ್ತದೆ.

    * ಒಂದೇ ಅಕ್ಷರವು ನಿರಂತರವಾಗಿ ಪುನರಾವರ್ತಿಸಿದರೆ:  
      ಅಕ್ಷರ + ಎಷ್ಟು ಬಾರಿ ಬಂದಿದೆ ಎಂಬ ಸಂಖ್ಯೆ
    * ಅಕ್ಷರವು ಒಂದೇ ಬಾರಿ ಬಂದರೆ:  
      ಅಕ್ಷರ ಮಾತ್ರ (ಸಂಖ್ಯೆ ಬರೆಯುವುದಿಲ್ಲ)

    ಉದಾಹರಣೆ:
        compress("aaabbc")   ->  "a3b2c"
        compress("abcd")     ->  "abcd"
        compress("")         ->  ""
    """
    if not s:                     # ಖಾಲಿ ಸ್ಟ್ರಿಂಗ್‌ಗಾಗಿ
        return ""

    result = []                   # ಫಲಿತಾಂಶವನ್ನು ಪಟ್ಟಿಯಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ
    count = 1                     # ಪ್ರಸ್ತುತ ಅಕ್ಷರದ ಎಣಿಕೆ
    prev = s[0]                   # ಹಿಂದಿನ ಅಕ್ಷರ

    for ch in s[1:]:
        if ch == prev:            # ಅದೇ ಅಕ್ಷರ ಬಂದರೆ ಎಣಿಕೆ ಹೆಚ್ಚಿಸಿ
            count += 1
        else:                     # ಬೇರೆ ಅಕ್ಷರ ಬಂದರೆ, ಹಿಂದಿನ ಅಕ್ಷರವನ್ನು ಬರೆಯಿರಿ
            result.append(prev)
            if count > 1:        # ಎಣಿಕೆ 1 ಕ್ಕಿಂತ ಹೆಚ್ಚಿದ್ದರೆ ಮಾತ್ರ ಸಂಖ್ಯೆ ಬರೆಯಿರಿ
                result.append(str(count))
            prev = ch            # ಹೊಸ ಅಕ್ಷರಕ್ಕೆ ಬದಲಾಯಿಸಿ
            count = 1            # ಎಣಿಕೆಯನ್ನು ಮರುಹೊಂದಿಸಿ

    # ಕೊನೆಯ ಗುಂಪನ್ನು ಸೇರಿಸಿ
    result.append(prev)
    if count > 1:
        result.append(str(count))

    return "".join(result)
```

### ಬಳಕೆ ಉದಾಹರಣೆ

```python
print(compress("aaabbc"))   # -> a3b2c
print(compress("abcd"))     # -> abcd
print(compress("zzzzzzzz")) # -> z8
print(compress("a"))        # -> a
print(compress(""))         # -> (ಖಾಲಿ)
```

---

#### ಪರ್ಯಾಯ: `itertools.groupby` ಬಳಸಿ

```python
from itertools import groupby

def compress_groupby(s: str) -> str:
    return "".join(
        f"{ch}{len(list(g)) if len(list(g)) > 1 else ''}"
        for ch, g in groupby(s)
    )
```

`groupby` ಬಳಸಿ ಕೋಡ್ ಸ್ವಲ್ಪ ಚಿಕ್ಕದಾಗುತ್ತದೆ, ಆದರೆ `list(g)` ಅನ್ನು ಎರಡು ಬಾರಿ ಕರೆಸುವ ಕಾರಣದಿಂದ ದೊಡ್ಡ ಸ್ಟ್ರಿಂಗ್‌ಗಳಿಗೆ ಸ್ವಲ್ಪ ನಿಧಾನವಾಗಬಹುದು.  

---

**ಸಾರಾಂಶ**  
- ಒಂದೇ ಅಕ್ಷರ ನಿರಂತರವಾಗಿ ಬಂದರೆ: `ಅಕ್ಷರ + ಎಣಿಕೆ`  
- ಒಂದೇ ಬಾರಿ ಬಂದರೆ: `ಅಕ್ಷರ` ಮಾತ್ರ  
- ಖಾಲಿ ಸ್ಟ್ರಿಂಗ್‌ಗೆ ಖಾಲಿ ಫಲಿತಾಂಶ.  

ಇದು ನಿಮ್ಮ “compress” ಅಗತ್ಯವನ್ನು ಪೂರೈಸುತ್ತದೆ!