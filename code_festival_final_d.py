from pprint import *
n = int(input())
if n == 1:
    exit(print(1, 1))
A = [[1], [1, 1]]
for i in range(10000):
    AA = [1]
    A2 = A[-1]
    for j in range(len(A2) - 1):
        if A2[j] + A2[j + 1] == n:
            exit(print(i + 3, j + 2))
        AA.append(A2[j] + A2[j + 1])
    A.append(AA + [1])
