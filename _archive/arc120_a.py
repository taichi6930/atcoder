from itertools import accumulate  # 累積和を求めるときに使う
n = int(input())
A = list(map(int, input().split()))
accAList = list(accumulate(A))
accaccAList = list(accumulate(accAList))
maxAList = [A[0]]
for i in range(1, n):
    maxAList.append(max(maxAList[-1], A[i]))

sumA = [A[0] * 2]

for i in range(1, n):
    sumA.append(accAList[i] + (i + 1) * maxAList[i] + accaccAList[i - 1])

for i in range(n):
    print(sumA[i])
