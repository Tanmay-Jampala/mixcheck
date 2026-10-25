def missing_number(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)