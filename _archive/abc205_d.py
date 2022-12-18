from bisect import bisect_right
n, q = map(int, input().split())
A = list(map(int, input().split()))
B = [[0]]
bNum = -1
K = [int(input()) for _ in range(q)]

dic = {}

for i in range(len(A)):
    if A[i] - B[-1][-1] == 1:
        B[-1].append(A[i])
        continue
    B.append([A[i]])

for b in B:
    bNum += len(b)
    dic[b[-1] + 1] = (b[-1] + 1) - bNum

dicKeys = list(dic.keys())
dicValues = list(dic.values())
for k in K:
    print(k
          - dicValues[bisect_right(dicValues, k) - 1]
          + dicKeys[bisect_right(dicValues, k) - 1])
