n, k = map(int, input().split())
A = list(map(int, input().split()))
print((1 + k) * k // 2 - sum(set([a for a in A if a <= k])))
