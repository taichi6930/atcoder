n, d = map(int, input().split())
T = list(map(int, input().split()))
for i in range(n - 1):
    if T[i + 1] - T[i] <= d:
        exit(print(T[i + 1]))
print(-1)
