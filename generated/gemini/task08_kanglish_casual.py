```python
def second_largest(numbers):
    if not numbers or len(numbers) < 2:
        return None

    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]
```