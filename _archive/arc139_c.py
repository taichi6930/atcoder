n, m = map(int, input().split())
t = [1 for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(i + 1, t[i])
        if t[i] > 3 + 1:
            t[i]
