```python
def remove_duplicates(input_list):
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]
```