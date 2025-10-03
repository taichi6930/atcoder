n = int(input())
A = list(map(int, input().split()))

print((min(A) + max(A)) * (n + 1) // 2 - sum(A))
