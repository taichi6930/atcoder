from collections import deque
from heapq import heapify, heappop, heappush
q = int(input())

heapifyCount = 0
A = []
heapify(A)
newList = deque([])

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        newList.append(query[1])
        continue

    if query[0] == 2:
        if heapifyCount > 0:
            print(heappop(A))
            heapifyCount -= 1
            continue
        print(newList.popleft())
        continue

    if query[0] == 3:
        for k in newList:
            heappush(A, k)
            heapifyCount += 1
        newList = deque([])
