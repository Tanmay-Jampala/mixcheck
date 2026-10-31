```python
def capitalize_words(sentence: str) -> str:
    # Convert the entire sentence to lowercase
    sentence = sentence.lower()
    # Split into words, ignoring any extra whitespace
    words = [w for w in sentence.split() if w]
    # Capitalize the first letter of each word
    capitalized = [w.capitalize() for w in words]
    # Join the words back together with a single space
    return ' '.join(capitalized)
```