def func(K):
    kMemo = K[0]
    kCnt = 1
    kList = []

    for i in range(1, len(K) + 1):
        if i == len(K):
            kList.append([kMemo, kCnt])
            break
        if kMemo != K[i]:
            kList.append([kMemo, kCnt])
            kMemo = K[i]
            kCnt = 1
            continue
        kCnt += 1
    return kList


S = list(input())
T = list(input())

sList = func(S)
tList = func(T)

if len(sList) != len(tList):
    exit(print('No'))

for i in range(len(sList)):
    sl = sList[i]
    tl = tList[i]
    if sl[0] != tl[0] or (sl[1] == 1 and tl[1] >= 2) or sl[1] > tl[1]:
        exit(print('No'))

print('Yes')
