Here’s a concise Python function that converts a temperature from Celsius to Fahrenheit using the standard formula \(F = C \times \frac{9}{5} + 32\):

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
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# Example usage:
if __name__ == "__main__":
    # Convert 0 °C, 25 °C, and 100 °C to Fahrenheit
    for c in (0, 25, 100):
        print(f"{c}°C → {celsius_to_fahrenheit(c)}°F")
```

**Explanation**

- The function accepts a numeric value (`int` or `float`) representing degrees Celsius.
- It applies the conversion formula `celsius * 9 / 5 + 32`.
- The result is returned as a `float`.
- The optional `if __name__ == "__main__":` block demonstrates how you might call the function and see the output.