t, n = map(int, input().split())
maxP = [0] * n

for i in range(t):
    p = list(map(int, input().split()))
    for j in range(n):
        maxP[j] = max(p[j], maxP[j])
    print(sum(maxP))
