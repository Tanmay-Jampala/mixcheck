# tests/task24.py
# Task: 2nd most frequent char, ignore spaces, case-sensitive, ties by first appearance
FUNCTION = "second_most_common"

CASES = [
    (["banana"], "n"),  # the example from the task
    (["aabbcc"], "b"),  # a three-way tie: first appearance decides
    (["a a a"], None),  # only one different character once spaces are ignored
    (["abc"], "b"),  # all appear once
    ([""], None),  # empty string
    (["Mississippi"], "s"),  # i and s tie at 4: i appears first, so s is second
    (["AaAa a"], "A"),  # a appears 3 times and A twice: capital and small are different
]
