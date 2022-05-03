n, q = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [A[i + 1] - A[i] - 1 for i in range(n)]
K = [int(input()) for _ in range(q)]

for i, k in enumerate(K):
    ans = 0
    for j, b in enumerate(B):
        if k - b <= 0:
            ans = A[j] + k
            k = 0
            break
        k -= b
    if ans == 0:
        ans = k + A[-1]
    print(ans)
