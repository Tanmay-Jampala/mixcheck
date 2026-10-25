```python
def valid_mobile(number_str):
    cleaned = "".join(number_str.split())
    if cleaned.startswith("+91"):
        cleaned = cleaned[3:]
    elif cleaned.startswith("0"):
        cleaned = cleaned[1:]
    return len(cleaned) == 10 and cleaned.isdigit() and cleaned[0] in "6789"
```