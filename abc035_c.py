from itertools import accumulate


def int2strWithArray(Array):
    return list(map(lambda x: str(x), Array))


n, q = map(int, input().split())
D = [0] * (n + 1)

for i in range(q):
    l, r = map(int, input().split())
    D[l - 1] += 1
    D[r] -= 1

accD = list(accumulate(D))
accD.pop()


print(''.join(int2strWithArray([k % 2 for k in accD])))
