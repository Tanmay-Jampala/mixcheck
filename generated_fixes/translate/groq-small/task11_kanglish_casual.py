Here’s a simple, type‑hinted Python function that converts Celsius to Fahrenheit:

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    Parameters
    ----------
    celsius : float
        Temperature in degrees Celsius.

    Returns
    -------
    float
        Temperature in degrees Fahrenheit.
    """
    return celsius * 9.0 / 5.0 + 32.0
```

You can use it like this:

```python
print(celsius_to_fahrenheit(0))   # 32.0
print(celsius_to_fahrenheit(100)) # 212.0
```

Feel free to adjust the type hints or add error handling if you need to support other input types.