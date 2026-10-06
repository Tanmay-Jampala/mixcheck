# tests/task09.py
# Task: count words in a string (extra spaces at start, end or between words are ignored)
FUNCTION = "count_words"

CASES = [
    (["hello world from Python"], 4),       # normal sentence (example from the task)
    ([""], 0),                              # empty string: no words
    (["   "], 0),                           # only spaces: no words, no empty words
    (["hello"], 1),                         # one word
    (["  hello   world  "], 2),             # extra spaces at start, end and between words
]
