n, p, q = map(int, input().split())
aList = list(map(int, input().split()))
ans = 0
for a1 in range(n - 4):
    for a2 in range(a1 + 1, n-3):
        for a3 in range(a2 + 1, n-2):
            for a4 in range(a3 + 1, n-1):
                for a5 in range(a4 + 1, n):
                    k = (((aList[a1] * aList[a2] % p) *
                         aList[a3] % p) * aList[a4] % p) * aList[a5] % p
                    if k == q:
                        ans += 1
print(ans)

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
Answer = 0

for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    v = ((((A[i] * A[j] % P) * A[k] %
                         P) * A[l] % P) * A[m]) % P
                    if v == Q:
                        Answer += 1

print(Answer)
