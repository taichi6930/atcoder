from heapq import heapify
from collections import defaultdict

n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
print(AB)
dic = defaultdict(list)
for i, [a, b] in enumerate(AB):
    print(a, b)
    dic[n - a + 1].append(b)
print(dic)
