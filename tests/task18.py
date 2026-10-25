# tests/task18.py
# Task: unique lowercase words, by length then alphabetically
FUNCTION = "sort_words"

CASES = [
    (["the Cat sat on the mat"], ["on", "cat", "mat", "sat", "the"]),  # the example from the task
    ([""], []),  # empty sentence
    (["Bb a B"], ["a", "b", "bb"]),  # capitals and ties
    (["Apple apple APPLE"], ["apple"]),  # same word in different cases
    (["zebra ant cat dog"], ["ant", "cat", "dog", "zebra"]),  # alphabetical within the same length
]
