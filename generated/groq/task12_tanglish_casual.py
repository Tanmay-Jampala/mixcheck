```python
def capitalize_words(sentence: str) -> str:
    """Capitalize the first letter of each word in a lowercase sentence."""
    # Split on single spaces, capitalize each word, then join back with spaces
    return " ".join(word.capitalize() for word in sentence.split(" "))
```