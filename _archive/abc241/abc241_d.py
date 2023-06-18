q = int(input())
queryList = [list(map(int, input().split())) for _ in range(q)]

for i, query in enumerate(queryList):
    x = query[1]
    if query[0] == 1:
        continue

    k = query[2]
    if query[0] == 2:
        continue
    if query[0] == 3:
        continue
