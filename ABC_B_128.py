n = int(input())
spList = [input().split() for _ in range(n)]
for i in range(n):
    spList[i][1] = 100 - int(spList[i][1])

for i in range(n):
    print(spList.index(sorted(spList)[i]) + 1)
