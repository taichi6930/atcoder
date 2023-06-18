n, x, y = map(int, input().split())
A = list(map(int, input().split()))

lrAminList = [A[0]]
rlAminList = [A[-1]]
lrAmaxList = [A[0]]
rlAmaxList = [A[-1]]

for i in range(n):
