import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = [300000 for _ in range(n)]
ans = 0


def Z(cnt, p, q):
    global ans, n, P, Q, R
    if p >= n or q >= n:
        ans = max(ans, cnt)
        return

    if (n - q + 1) + cnt < ans or (n - p + 1) + cnt < ans:
        return

    if R[cnt] < q:
        return

    if Q[q] % P[p] == 0:
        R[cnt] = max(q, R[cnt])
        cnt += 1
        p += 1
        q += 1
        Z(cnt, p, q)
        return

    Z(cnt, p + 1, q)
    Z(cnt, p, q + 1)


Z(0, 0, 0)
print(ans)
