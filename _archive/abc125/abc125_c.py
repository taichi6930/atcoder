from math import gcd
n = int(input())
A = list(map(int, input().split()))

leftgcd = [A[0]] + [None for _ in range(n - 1)]
rightgcd = [None for _ in range(n - 1)] + [A[-1]]

for i in range(n - 1):
    leftgcd[i + 1] = gcd(leftgcd[i], A[i + 1])
    rightgcd[n - i - 2] = gcd(rightgcd[n - i - 1], A[n - i - 2])

ans = 1

for j in range(n):
    a, b = j - 1, j + 1
    k = 0
    if a < 0:
        k = rightgcd[b]
    elif b >= n:
        k = leftgcd[a]
    else:
        k = gcd(leftgcd[a], rightgcd[b])
    ans = max(k, ans)

print(ans)
