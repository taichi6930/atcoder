from collections import Counter

n, m = map(int, input().split())
ALow = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    ALow[b - 1] += 1

print(Counter(ALow)[1])
