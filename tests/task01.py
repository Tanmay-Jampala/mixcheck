# tests/task01.py
# Task: reverse a string
FUNCTION = "reverse_string"

CASES = [
    (["hello"], "olleh"),                   # normal word
    ([""], ""),                             # empty string: the tricky case
    (["a"], "a"),                           # one character
    (["Hello World"], "dlroW olleH"),       # spaces and capitals
    (["abc123"], "321cba"),                 # letters and digits
]
