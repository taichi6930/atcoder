import sys
sys.setrecursionlimit(500000)

n = int(input())
time = {}
kList = {}

for i in range(n):
    q = list(map(int, input().split()))
    t, k, A = q[0], q[1], q[2:]
    time[i + 1] = t
    kList[i + 1] = A

ansList = set([n])


def test(lis):
    global ansList
    for a in lis:
        if a in ansList:
            continue
        ansList.add(a)
        if a in kList:
            test(kList[a])


test(kList[n])

print(sum([time[ans] for ans in ansList]))
