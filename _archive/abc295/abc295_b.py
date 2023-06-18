from pprint import pprint
from copy import deepcopy
R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
K = deepcopy(B)

for r in range(R):
    for c in range(C):
        a = B[r][c]
        if a in ['#', '.']:
            continue
        a = int(a)
        for r1 in range(R):
            for c1 in range(C):
                if abs(r1 - r) + abs(c1 - c) <= a:
                    K[r1][c1] = '.'

for k in K:
    print(''.join(k))
