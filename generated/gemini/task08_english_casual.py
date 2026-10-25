```python
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first = second = float("-inf")
    for n in numbers:
        if n > first:
            second, first = first, n
        elif n > second:
            second = n
    return second if second != float("-inf") else None
```