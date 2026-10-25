def capitalize_words(sentence: str) -> str:
    return ' '.join(word.capitalize() for word in sentence.split(' '))