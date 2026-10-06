```python
def second_largest(numbers):
    if len(set(numbers)) < 2:
        return None
    unique_numbers = sorted(list(set(numbers)), reverse=True)
    return unique_numbers[1]
```