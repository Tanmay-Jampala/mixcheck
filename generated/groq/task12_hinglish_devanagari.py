```python
def capitalize_words(sentence: str) -> str:
    """
    Convert a lowercase sentence to title case, capitalizing the first letter of each word.
    
    Parameters:
        sentence (str): A sentence with words separated by single spaces.
    
    Returns:
        str: The sentence with each word's first character in uppercase.
    """
    # Split the sentence into words, capitalize each, then join back with spaces
    return ' '.join(word.capitalize() for word in sentence.split(' '))
```