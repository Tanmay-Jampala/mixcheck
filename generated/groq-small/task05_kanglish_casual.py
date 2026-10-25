**Python ನಲ್ಲಿ ಒಂದು ಲಿಸ್ಟ್‌ನಿಂದ ಡ್ಯುಪ್ಲಿಕೇಟ್ ಅಂಶಗಳನ್ನು ತೆಗೆದು ಹಾಕುವ ಫಂಕ್ಷನ್**  
(ಮೂಲ ಕ್ರಮ (ಆರ್ಡರ್) ಅದೇ ಇರಲಿ, ಹೊಸ ಲಿಸ್ಟ್ ಹಿಂತಿರುಗಿಸಲಿ)

```python
def remove_duplicates(seq):
    """
    seq: ಯಾವುದೇ iterable (ಸಾಮಾನ್ಯವಾಗಿ list)
    ಹಿಂತಿರುಗಿಸುವುದು: ಮೂಲ ಕ್ರಮವನ್ನು ಉಳಿಸಿಕೊಂಡು, ಡ್ಯುಪ್ಲಿಕೇಟ್‌ಗಳಿಲ್ಲದ ಹೊಸ ಲಿಸ್ಟ್
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### ಬಳಕೆ ಉದಾಹರಣೆ

```python
original = [3, 5, 2, 3, 8, 5, 1, 2]
unique = remove_duplicates(original)
print(unique)          # Output: [3, 5, 2, 8, 1]
```

### ವಿವರಣೆ

1. **`seen`** – ಈಗಾಗಲೇ ಕಂಡುಬಂದ ಅಂಶಗಳ ಸೆಟ್.  
2. **`result`** – ಕ್ರಮವನ್ನು ಉಳಿಸಿಕೊಂಡು ಹೊಸ ಲಿಸ್ಟ್.  
3. ಪ್ರತಿ ಅಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ, ಅದು `seen` ನಲ್ಲಿ ಇಲ್ಲದಿದ್ದರೆ ಮಾತ್ರ `result` ಗೆ ಸೇರಿಸಿ ಮತ್ತು `seen` ಗೆ ಸೇರಿಸಿ.  
4. ಅಂತಿಮವಾಗಿ `result` ಅನ್ನು ಹಿಂತಿರುಗಿಸಿ.

> **ಗಮನಿಸಿ**:  
> - ಈ ವಿಧಾನವು **ಅಂಶಗಳು ಹ್ಯಾಶ್ ಮಾಡಬಹುದಾದ** (hashable) ಆಗಿರಬೇಕು (ಉದಾ: int, str, tuple).  
> - ಲಿಸ್ಟ್‌ನಲ್ಲಿರುವ ಅಂಶಗಳು ಹ್ಯಾಶ್ ಮಾಡಲಾಗದಿದ್ದರೆ (ಉದಾ: list, dict) `seen` ಬಳಸಲು ಸಾಧ್ಯವಿಲ್ಲ; ಆ ಸಂದರ್ಭದಲ್ಲಿ `list.index()` ಅಥವಾ `collections.OrderedDict` ಬಳಸಬಹುದು.  

```python
# ಹ್ಯಾಶ್ ಮಾಡಲಾಗದ ಅಂಶಗಳಿಗಾಗಿ (ಉದಾ: list ಒಳಗೆ list)
def remove_duplicates_unhashable(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result
```

ಇದು ನಿಮ್ಮ ಅಗತ್ಯಕ್ಕೆ ಸರಿಹೊಂದುತ್ತದೆ ಎಂದು ಭಾವಿಸುತ್ತೇನೆ! ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ ಕೇಳಿ.