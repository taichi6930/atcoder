n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
LI = []

for i in range(n):
    LI.append([A[i] + B[i], A[i], i + 1])

LI = sorted(LI, reverse=True, key=lambda x: x[1])
LI = sorted(LI, reverse=True, key=lambda x: x[0])

print(" ".join([str(LI[i][2]) for i in range(n)]))
