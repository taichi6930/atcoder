from itertools import *
from pprint import *
from collections import *
h, w = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = []
for i in range(h):
    A += list(map(int, input().split()))
cA = Counter(A)


def func(score, lisP, setP):
    for i in range(10):
        if i in setP:
            continue
        newScore = score + C[lisP[-1]][i]
        if C[lisP[0]][i] < newScore:
            continue
        C[lisP[0]][i] = newScore
        newLisP = lisP + [i]
        newSetP = setP | set([i])
        func(newScore, newLisP, newSetP)


for i in range(10):
    func(0, [i], set([i]))

print(sum([cA[i] * C[i][1] for i in range(10)]))
