n = int(input())
A = list(map(int, input().split()))
ANS = []

for i in range(n - 1):
    x, y = A[i], A[i + 1]
    ANS += range(x, y, 1 if x < y else -1)

ANS.append(A[-1])
print(*ANS)
