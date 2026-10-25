```python
def valid_mobile(number_str):
    if not isinstance(number_str, str):
        return False
    
    # Shob space shoriye dewa
    clean_str = "".join(number_str.split())
    
    # "+91" ba "0" prefix shoriye dewa
    if clean_str.startswith("+91"):
        clean_str = clean_str[3:]
    elif clean_str.startswith("0"):
        clean_str = clean_str[1:]
        
    # Check kora ja baki thake sheta exactly 10 digits kina aar 6, 7, 8, 9 diye shuru kina
    if len(clean_str) == 10 and clean_str.isdigit() and clean_str[0] in "6789":
        return True
        
    return False
```