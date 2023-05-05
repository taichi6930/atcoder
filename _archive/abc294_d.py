from collections import deque
n, q = map(int, input().split())
ll = deque([i for i in range(1, n + 1)])
for _ in range(q):
    event = list(map(int, input().split()))
    t = event[0]
    if t == 1:
