# 繰り返しのテレポーター問題
n, k = map(int, input().split())
A = list(map(int, input().split()))
ansSet = set([1])
ansList = [1]
l = 1
swi = False

for i in range(k):
    l = A[l - 1]
    if l in ansSet:
        swi = True
        break
    ansSet.add(l)
    ansList.append(l)

if swi:
    a = ansList.index(l)
    k -= a
    k %= len(ansList[a:])
    print(ansList[k + a])
else:
    print(ansList[-1])
