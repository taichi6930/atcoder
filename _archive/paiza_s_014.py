from collections import defaultdict
n = int(input())
dic = defaultdict()
for _ in range(n):
    x, y, z, w, h, v = map(int, input().split())
    dic[f'{z}-{z + v - 1}'] = f'{}'
