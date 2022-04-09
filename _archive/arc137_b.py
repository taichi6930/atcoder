from collections import Counter, deque
from itertools import accumulate  # 累積和を求めるときに使う

n = int(input())
a = input()
areplace = a.replace('1', '-1').replace('0', '1')
A = list(map(int, a.split()))
A2 = list(map(int, areplace.split()))
sumA = sum(A)
B = [0] + list(accumulate(A))
B2 = [0] + list(accumulate(A2))

minAns, maxAns = sumA, sumA
minB2 = [B2[1]]
maxB2 = [B2[1]]

for i in range(n - 1):
    minB2.append(min(minB2[-1], B2[i + 2]))
    maxB2.append(max(maxB2[-1], B2[i + 2]))

print(B, minB2, maxB2)

for i in range(n):
    x, y, z = B[i + 1], minB2[i], maxB2[i]
    minAns = min(minAns, x + y)
    maxAns = max(maxAns, x + z)


print(maxAns - minAns + 1, maxAns, minAns)
