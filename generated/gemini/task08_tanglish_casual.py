```python
def second_largest(venum):
    if len(venum) < 2:
        return None

    ulappu = list(set(venum))
    if len(ulappu) < 2:
        return None

    ulappu.sort()
    return ulappu[-2]
```