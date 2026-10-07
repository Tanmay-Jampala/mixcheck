FUNCTION = "word_count"

# Order inside a dictionary doesn't matter: {"a": 2, "b": 1} == {"b": 1, "a": 2}
CASES = [
    (["a b a"], {"a": 2, "b": 1}),                                # the example from the task
    (["hello"], {"hello": 1}),                                    # single word
    ([""], {}),                                                   # empty sentence: the tricky case
    (["the cat the hat the"], {"the": 3, "cat": 1, "hat": 1}),    # one word repeated 3 times
    (["go go go"], {"go": 3}),                                    # every word is the same
]
