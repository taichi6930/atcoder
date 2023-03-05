n, m = map(int, input().split())
A = [int(input()) for _ in range(n - 1)]

print(sum([a for a in A if a <= m]))
