```python
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
            
    return second
```