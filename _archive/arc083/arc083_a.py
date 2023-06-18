from math import gcd
from bisect import bisect_left
a, b, c, d, e, f = map(int, input().split())

waterSet = set()
sugerSet = set()

for i in range(100):
    for j in range(100):
        water = 100 * (a * i + b * j)
        if water > f:
            break
        waterSet.add(water)

for i in range(4000):
    for j in range(4000):
        suger = (c * i + d * j)
        if suger > f:
            break
        sugerSet.add(suger)

waterList = sorted(list(waterSet))
sugerList = sorted(list(sugerSet))

ansList = []
ansSet = set()

for water in waterList:
    s = water * e / 100
    k = bisect_left(sugerList, min(s, f - water))
    for i in range(max(0, k - 2), min(k + 3, len(sugerList))):
        suger = sugerList[i]
        if e * water - 100 * suger >= 0:
            if suger == 0:
                if '1-0' in ansSet:
                    continue
                ansList.append([1, 0])
                ansSet.add('1-0')
                continue
            if water + suger > f:
                continue
            kgcd = gcd(water + suger, suger)
            st = str((water + suger) // kgcd) + '-' + str((suger) // kgcd)
            if st in ansSet:
                continue
            ansList.append([(water + suger), (suger)])
            ansSet.add(st)


def int2strWithArray(Array):  # 数字の配列を文字の配列に変換する
    return list(map(lambda x: str(x), Array))


ans = [min(a, b) * 100, 0]

for ans1 in ansList:
    if ans[1] * ans1[0] < ans[0] * ans1[1]:
        ans = ans1
print(' '.join(int2strWithArray(ans)))
