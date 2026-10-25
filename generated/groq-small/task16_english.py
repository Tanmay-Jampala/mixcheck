def indian_format(n: int) -> str:
    s = str(n)
    if len(s) <= 3:
        return s
    last3 = s[-3:]
    rest = s[:-3]
    rev = rest[::-1]
    groups = [rev[i:i+2] for i in range(0, len(rev), 2)]
    rest_formatted = ','.join(groups)[::-1]
    return f"{rest_formatted},{last3}"