from pprint import pprint
from collections import defaultdict
n, x, f, s = map(int, input().split())
parent_dict = defaultdict(list)


def func(cnt):
    for k, v in sorted(parent_dict[cnt].items(), reverse=True):
        if not cnt + 3 in list(parent_dict.keys()):
            parent_dict[cnt + 3] = defaultdict(int)
        if not cnt + 1 in list(parent_dict.keys()):
            parent_dict[cnt + 1] = defaultdict(int)
        parent_dict[cnt + 3][k] = min(v + s, x)
        if v - f >= 0:
            parent_dict[cnt + 1][k + v] += v - f
    if cnt == 5:
        exit()
    pprint(parent_dict)
    func(cnt + 1)


parent_dict[0] = defaultdict(int)
parent_dict[0][0] = x
func(0)
