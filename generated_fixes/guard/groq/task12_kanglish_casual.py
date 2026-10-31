```python
def capitalize_words(sentence: str) -> str:
    """
    Convert a lowercase sentence into title case.

    Parameters:
        sentence (str): A string containing words separated by spaces,
                        all in lowercase.

    Returns:
        str: The sentence with the first letter of each word capitalized.
    """
    # Split the sentence into words, capitalize each, then join back.
    return ' '.join(word.capitalize() for word in sentence.split())
```