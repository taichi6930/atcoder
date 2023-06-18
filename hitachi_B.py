a, b, m = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
minAB = min(listA) + min(listB)
for i in range(m):
    x, y, c = map(int, input().split())
    minAB = min(minAB, listA[x - 1] + listB[y - 1] - c)
print(minAB)
