mod = 10 ** 9 + 7

n, k = map(int, input().split())
A = list(map(int, input().split()))

ansAin = 0
ansAout = 0

for i in range(n):
    for j in range(n):
        if A[i] > A[j]:
            ansAout += 1
            if i < j:
                ansAin += 1

print((ansAin * k + ansAout * k * (k - 1) // 2) % mod)
