FUNCTION = "capitalize_words"

CASES = [
    (["hello world"], "Hello World"),                  # the example from the task
    (["python"], "Python"),                            # single word
    ([""], ""),                                        # empty sentence: the tricky case
    (["a b c"], "A B C"),                              # single-letter words
    (["the quick brown fox"], "The Quick Brown Fox"),  # more than two words
]
