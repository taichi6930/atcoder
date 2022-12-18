n = int(input())
lis = [int(input()) for _ in range(5)]
minLis = min(lis)
minLisIndex = lis.index(minLis)
ans = (n + minLis - 1) // minLis
print(ans + 4)
