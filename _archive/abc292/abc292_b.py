from collections import defaultdict
n, q = map(int, input().split())
dic = defaultdict(int)
for _ in range(q):
    k, x = map(int, input().split())
    if k == 1:
        dic[x] += 1
        continue
    if k == 2:
        dic[x] = 2
        continue
    if k == 3:
        print('YNeos'[(dic[x] < 2)::2])
