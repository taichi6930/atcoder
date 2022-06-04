from collections import Counter
n, m = map(int, input().split())
S = [list(map(int, input().split()))[1:] for _ in range(m)]
P = list(map(int, input().split()))


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


ansList = Counter()


def is_nth_bit_set(num: int, k: int):
    if num & (1 << k):
        return True
    return False


for i in range(2 ** n):
    aSet = set()
    for j in range(n):
        if is_nth_bit_set(i, j):
            continue
        aSet.add(j + 1)
    swi = True
    Q = [0] * m
    for k, s in enumerate(S):
        cnt = 0
        for a in list(aSet):
            if a in set(s):
                cnt = (cnt + 1) % 2
        Q[k] = cnt
    ansList[''.join(int2strWithArray(Q))] += 1

print(ansList[''.join(int2strWithArray(P))])
