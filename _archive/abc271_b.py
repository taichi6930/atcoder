n, q = map(int, input().split())
L = [list(map(int, input().split()))[1:] for _ in range(n)]

for _ in range(q):
    s, t = map(int, input().split())
    print(L[s - 1][t - 1])
