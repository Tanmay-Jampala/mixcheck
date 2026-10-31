**Python‑ನಲ್ಲಿ “count_words” ಎಂಬ ಫಂಕ್ಷನ್ ಬರೆಯುವ ಸರಳ ವಿಧಾನ**

```python
def count_words(text: str) -> int:
    """
    ಕೊಟ್ಟಿರುವ string‑ನಲ್ಲಿ ಎಷ್ಟು ಪದಗಳಿವೆ ಎಂದು ಎಣಿಸುತ್ತದೆ.

    ಪದಗಳು ಎಂದರೆ space (ಅಥವಾ ಯಾವುದೇ whitespace) ಮೂಲಕ ಬೇರ್ಪಡಿಸಿದ non‑empty
    ಭಾಗಗಳು.  ಆರಂಭ/ಅಂತ್ಯದಲ್ಲಿರುವ extra spaces, ಅಥವಾ ಮಧ್ಯದಲ್ಲಿರುವ
    ಅನೇಕ spaces ಗಳನ್ನು ನಿರ್ಲಕ್ಷಿಸಲಾಗುತ್ತದೆ.

    Parameters
    ----------
    text : str
        ಪದಗಳನ್ನು ಎಣಿಸಬೇಕಾದ string.

    Returns
    -------
    int
        ಪದಗಳ ಸಂಖ್ಯೆ.
    """
    # 1. split() ಬಳಸಿದರೆ, ಯಾವುದೇ whitespace (space, tab, newline) ಗಳಲ್ಲಿ
    #    ಬೇರ್ಪಡಿಸಿ, ಖಾಲಿ string ಗಳನ್ನು ಸ್ವಯಂ ತೆಗೆದುಹಾಕುತ್ತದೆ.
    # 2. split(' ') ಬಳಸಿದರೆ, ಕೇವಲ space‑ಗಳಲ್ಲೇ ಬೇರ್ಪಡಿಸಿ, ಖಾಲಿ string
    #    ಗಳನ್ನು ಕೈಯಾರೆ ಫಿಲ್ಟರ್ ಮಾಡಬೇಕು.
    # ಇಲ್ಲಿ split() ನ್ನೇ ಬಳಸುತ್ತಿದ್ದೇವೆ – ಇದು ಹೆಚ್ಚು ಸಾಮಾನ್ಯ.

    words = text.split()          # ['Hello', 'world', 'Python']
    return len(words)
```

### ಉದಾಹರಣೆಗಳು

```python
print(count_words("Hello world"))          # 2
print(count_words("  Hello   world  "))    # 2
print(count_words("one two   three"))      # 3
print(count_words(""))                     # 0
print(count_words("   "))                  # 0
```

### ಪರ್ಯಾಯ: `re` (regular expressions) ಬಳಸಿ

```python
import re

def count_words_regex(text: str) -> int:
    # \S+  : 1 ಅಥವಾ ಹೆಚ್ಚಿನ non‑whitespace ಅಕ್ಷರಗಳ ಗುಂಪು
    return len(re.findall(r'\S+', text))
```

`re.findall(r'\S+', text)` ಕೂಡ ಖಾಲಿ string ಗಳನ್ನು ಹೊರತುಪಡಿಸಿ, ಯಾವುದೇ whitespace‑ನಲ್ಲಿ ಬೇರ್ಪಡಿಸಿದ ಪದಗಳ ಪಟ್ಟಿಯನ್ನು ನೀಡುತ್ತದೆ.

---

**ಸಾರಾಂಶ**  
- `split()` (ಅಥವಾ `split(' ')` + ಫಿಲ್ಟರ್) ಬಳಸಿ, ಆರಂಭ/ಅಂತ್ಯ/ಮಧ್ಯದ extra spaces ಗಳನ್ನು ನಿರ್ಲಕ್ಷಿಸಿ, ಸರಳವಾಗಿ ಪದಗಳ ಸಂಖ್ಯೆಯನ್ನು ಪಡೆಯಬಹುದು.  
- `re.findall(r'\S+', text)` ಕೂಡ ಅದೇ ಕೆಲಸ ಮಾಡುತ್ತದೆ, ಆದರೆ regex ಬಳಸುವಾಗ ಸ್ವಲ್ಪ ಹೆಚ್ಚು ಕೋಡ್ ಬರೆಯಬೇಕಾಗಬಹುದು.  

ಇದರಿಂದ ನಿಮ್ಮ “count_words” ಫಂಕ್ಷನ್ ಸಂಪೂರ್ಣವಾಗಿ ಸಿದ್ಧ! 🚀