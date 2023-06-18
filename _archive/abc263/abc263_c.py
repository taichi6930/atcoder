n, m = map(int, input().split())


def t(cnt, lis):
    global n, m
    if cnt == n:
        print(* lis[1:])
        return
    for i in range(lis[-1] + 1, m + 1):
        t(cnt + 1, lis + [i])


t(0, [0])
