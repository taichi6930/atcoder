from collections import Counter

n, m = map(int, input().split())
ans = 0
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

print(sum([P[D.index(c) + 1 if c in D else 0] for i, c in enumerate(C)]))
