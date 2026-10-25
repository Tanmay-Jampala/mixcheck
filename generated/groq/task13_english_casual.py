```python
import string
from collections import Counter

def word_count(sentence: str) -> dict:
    # Lowercase
    s = sentence.lower()
    # Remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    # Normalize whitespace to single spaces
    s = ' '.join(s.split())
    # Count words
    return dict(Counter(s.split()))
```