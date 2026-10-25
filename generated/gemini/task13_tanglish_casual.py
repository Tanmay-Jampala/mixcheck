```python
import string


def word_count(sentence):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_sentence = sentence.lower().translate(translator)
    words = cleaned_sentence.split()

    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict
```