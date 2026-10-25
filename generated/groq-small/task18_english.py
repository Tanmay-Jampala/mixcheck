def sort_words(sentence):
    if not sentence:
        return []
    words = sentence.split()
    unique_words = set(word.lower() for word in words)
    return sorted(unique_words, key=lambda w: (len(w), w))