from collections import defaultdict
S = input()
dic = defaultdict()


def f(Str):
    d = defaultdict()
    cnt = 0
    st = None
    gl = None

    for i, s in enumerate(Str):
        if s == '(':
            if cnt == 0:
                st = i
            cnt += 1
            continue
        if s == ')':
            cnt -= 1
            if cnt != 0:
                continue
            gl = i
            print(Str[st + 1: gl])
            f(Str[st + 1: gl])

    return d


print(f(S))
