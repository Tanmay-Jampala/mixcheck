**Python function – `remove_duplicates`**

```python
def remove_duplicates(seq):
    """
    ಕೊಟ್ಟಿರುವ iterable (list, tuple, string …) ನಿಂದ
    ಪುನರಾವರ್ತಿತ (duplicate) ಅಂಶಗಳನ್ನು ತೆಗೆದು,
    ಮೂಲ ಕ್ರಮ (order) ಉಳಿಸಿಕೊಂಡು ಹೊಸ list ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.

    Parameters
    ----------
    seq : iterable
        duplicate ಗಳನ್ನು ತೆಗೆದುಹಾಕಬೇಕಾದ ಮೂಲ data.

    Returns
    -------
    list
        ಕ್ರಮ ಉಳಿದ, duplicate ಇಲ್ಲದ ಹೊಸ list.
    """
    seen = set()          # ಈಗಾಗಲೇ ಬಂದ ಅಂಶಗಳ ಸಂಗ್ರಹ
    result = []           # ಫಲಿತಾಂಶ list

    for item in seq:
        if item not in seen:   # ಮೊದಲ ಬಾರಿಗೆ ಬಂದಿದ್ದರೆ
            seen.add(item)     # ನೆನಪಿನಲ್ಲಿ ಇಟ್ಟು
            result.append(item)   # ಫಲಿತಾಂಶಕ್ಕೆ ಸೇರಿಸು
    return result
```

### ಹೇಗೆ ಬಳಸುವುದು

```python
>>> original = [3, 5, 2, 3, 7, 5, 2, 9, 3]
>>> clean = remove_duplicates(original)
>>> print(clean)
[3, 5, 2, 7, 9]
```

- **ಕ್ರಮ ಉಳಿದಿದೆ** – ಮೊದಲ ಬಾರಿಗೆ ಬಂದ ಅಂಶಗಳು ಮಾತ್ರ ಉಳಿದು, ಅವುಗಳ ಮೂಲ ಸ್ಥಾನ ಕ್ರಮವೂ ಉಳಿದಿದೆ.  
- **ಹೊಸ list** – ಮೂಲ `original` list ಬದಲಾಗುವುದಿಲ್ಲ; `clean` ಎಂಬ ಹೊಸ list ಅನ್ನು ಪಡೆಯುತ್ತೀರಿ.  

---

### ಇನ್ನೊಂದು ಸಂಕ್ಷಿಪ್ತ ರೂಪ (Python 3.7+)

Python 3.7‑ನಿಂದ `dict` ಗಳಲ್ಲಿ ಸೇರಿಸುವ ಕ್ರಮವನ್ನು ನೆನಪಿಡುತ್ತದೆ, ಆದ್ದರಿಂದ ಈ ರೀತಿಯ ಒಂದು ಸಾಲಿನ ಪರಿಹಾರವೂ ಇದೆ:

```python
def remove_duplicates(seq):
    return list(dict.fromkeys(seq))
```

ಇದು ಮೇಲಿನ ದೀರ್ಘ ರೂಪದಂತೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ, ಆದರೆ `dict`‑ನ ಒಳಗಿನ ಕ್ರಮ‑ಸಂಗ್ರಹಣೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿರುವುದರಿಂದ Python 3.7 ಮತ್ತು ಅದರ ಮೇಲಿನ ಆವೃತ್ತಿಗಳಲ್ಲಿ ಮಾತ್ರ ಸುರಕ್ಷಿತ.  

---

**ಗಮನಿಸಿ:**  
- ಇನ್‌ಪುಟ್ iterable ನಲ್ಲಿ **hashable** (ಹ್ಯಾಶ್ ಮಾಡಬಹುದಾದ) ಅಂಶಗಳು ಇರಬೇಕು, ಏಕೆಂದರೆ `set`/`dict` ಅವುಗಳನ್ನು ಕೀ ಆಗಿ ಬಳಸುತ್ತವೆ.  
- ಅಹ್ಯಾಶ್ ಮಾಡಬಹುದಾದ (unhashable) ಅಂಶಗಳು (ಉದಾ: ಇನ್ನೊಂದು list) ಇದ್ದರೆ, ಮೇಲಿನ ಮೊದಲ ದೀರ್ಘ ರೂಪವನ್ನು `seen` ಅನ್ನು `list` ಆಗಿ ಬದಲಿಸಿ (O(n²) ಸಮಯ) ಬಳಸಬಹುದು, ಅಥವಾ `collections.OrderedDict`‑ನ `popitem`‑ನ್ನು ಬಳಸುವ ಇನ್ನೊಂದು ತಂತ್ರವನ್ನು ಆಯ್ಕೆ ಮಾಡಬಹುದು.  

ಇದು ನಿಮಗೆ ಬೇಕಾದ `remove_duplicates` ಫಂಕ್ಷನ್. Happy coding! 🚀