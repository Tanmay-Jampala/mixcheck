```python
import string


def word_count(sentence):
    translator = str.maketrans("", "", string.punctuation)
    clean_sentence = sentence.lower().translate(translator)
    words = clean_sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
```