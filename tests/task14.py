FUNCTION = "are_anagrams"

# Two inputs: both go inside the same list
CASES = [
    (["listen", "silent"], True),   # the example from the task
    (["hello", "world"], False),    # not an anagram
    (["", ""], True),               # both empty
    (["aab", "abb"], False),        # same letters, different counts: the tricky case
    (["abc", "ab"], False),         # different lengths
]
