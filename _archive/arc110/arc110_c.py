from bisect import bisect_left
n = int(input())
P = list(map(int, input().split()))
L = [i for i in range(n)]
print(L)
cnt = 0

for i in range(n):
    c = bisect_left(P, i + 1)
    print(c)
