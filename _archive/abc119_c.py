from copy import deepcopy
from collections import Counter
from bisect import bisect_left

n, a, b, c = map(int, input().split())
lList = sorted([int(input()) for _ in range(n)], reverse=True)
abcList = [a, b, c]

mpMin = 10000
clList = Counter(lList)


def depth(clList, cnt, mp):
    global a, b, c, mpMin, abclist
    if mp >= mpMin:
        return
    if cnt == 3:
        mpMin = min(mpMin, mp)
        return

    # 対象となるkeyを選ぶ
    keys = list(clList.keys())
    values = list(clList.values())
    if cnt + sum(values) < 3:
        return
    # print(clList, cnt, mp)

    # 対象になる竹を選定する
    k = abcList[cnt]

    # 竹を増減して行く
    for key in keys:
        newClList = deepcopy(clList)
        mpKey = abs(key - k)
        newClList[key] -= 1
        if newClList[key] <= 0:
            newClList.pop(key)
        depth(newClList, cnt + 1, mp + mpKey)

    # for key1 in keys:
    #     for key2 in keys:
    #         if key1 == key2 and clList[key1] < 2:
    #             continue
    #         newClList = deepcopy(clList)
    #         newClList[key1] -= 1
    #         if newClList[key1] <= 0:
    #             newClList.pop(key1)
    #         newClList[key2] -= 1
    #         if newClList[key2] <= 0:
    #             newClList.pop(key2)
    #         if key1 + key2 <= k:
    #             newClList[key1 + key2] += 1
    #         depth(newClList, cnt, mp + 10)


depth(clList, 0, 0)

print(mpMin)
