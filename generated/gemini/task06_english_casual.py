```python
def sum_even_numbers(numbers: list[int]) -> int:
    return sum(n for n in numbers if n % 2 == 0)
```