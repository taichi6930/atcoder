n, k = map(int, input().split())
aList = list(map(int, input().split()))

ans = 1


for i in range(n):
    if ans + i > n:
        break
    aListEx = aList[i: ans + i]
    aSet = set(aListEx)
    # print(aListEx, aSet)
    for j in range(ans + i, n + 1):
        # if ans + j > n:
        #     break
        aSet.add(aList[j])
        print(aList[i: j + 1], aSet, i, j)
        #     if len(aSet) > k:
        #         break
        #     ans = max(j - i + 1, ans)

    pass
print(ans)
