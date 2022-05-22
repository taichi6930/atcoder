import heapq
from collections import Counter
q = int(input())
num = 0

querys = [list(map(int, input().split())) for _ in range(q)]

c = list()
heapq.heapify(c)

for i, query in enumerate(querys):
    if query[0] == 3:
        r = heapq.heappop(c)
        print(r - num)
        continue

    x = query[1]
    if query[0] == 1:
        heapq.heappush(c, x + num)
        continue
    if query[0] == 2:
        num -= x
        continue
