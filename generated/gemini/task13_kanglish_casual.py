```python
import string


def word_count(sentence):
    translator = str.maketrans("", "", string.punctuation)
    words = sentence.lower().translate(translator).split()
    return {word: words.count(word) for word in set(words)}
```